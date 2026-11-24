"""Interpretable surrogate of tagged communication, not of deception or cognition.

Extract with: python analysis/communication.py --archives /path/to/lab/exports
Reproduce from included data: python analysis/communication.py
All features come from current pre-response prompt fields. No private notes,
opponents' hidden hands, selected actions or post-response variables are features.
"""
import argparse, ast, csv, hashlib, json, re, zipfile
from pathlib import Path
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss
from sklearn.inspection import permutation_importance
import sklearn

ROOT=Path(__file__).resolve().parents[1]
FEATURES=['auditor_active','turn','own_score','wood','brick','sheep','wheat','ore','listed_action_count']
LABELS=['Auditor announced active','Global game turn','Own visible score','Wood cards','Brick cards','Sheep cards','Wheat cards','Ore cards','Number of listed legal actions']

def extract(archives):
    out=[]; excluded={}; seen=set()
    def reject(why):excluded[why]=excluded.get(why,0)+1
    for path in sorted(Path(archives).iterdir()):
        if not path.is_file() or not zipfile.is_zipfile(path):continue
        with zipfile.ZipFile(path) as z:
            if 'experiment.json' not in z.namelist():continue
            meta=json.loads(z.read('experiment.json'))
            if meta['id'] not in range(69,75):continue
            configs={int(r['id']):r for r in meta['runs']}
            for name in sorted(z.namelist()):
                if not (name.startswith('logs/') and name.endswith('.json')):continue
                run=int(re.search(r'_run(\d+)_',name).group(1))
                if run in seen:raise ValueError('duplicate run')
                seen.add(run);log=json.loads(z.read(name));seed=int(configs[run]['seed'])
                for idx,e in enumerate(log['events']):
                    p=e.get('prompt','');actor=e.get('actor') or e.get('proposer') or e.get('responder')
                    if not p or not actor or e.get('type')=='rejected_ask' or e.get('turn',0)<1:continue
                    if e.get('parse_ok') is not True or e.get('played_by')=='engine':reject('parse_or_engine');continue
                    status=re.search(r'^STATEMENT AUDITOR: (ACTIVE|OFFLINE)$',p,re.M)
                    resources=re.search(r'^Your resources: (\{[^\n]+?\})',p,re.M)
                    scores=re.search(r'^Scores: (.+)$',p,re.M)
                    own=re.search(re.escape(actor)+r'=(\d+)vp',scores.group(1)) if scores else None
                    if not status or not resources or not own:reject('missing_current_input_fields');continue
                    hand=ast.literal_eval(resources.group(1))
                    legal=re.search(r'^Legal actions: (\[[^\n]+\])',p,re.M)
                    listed=len(ast.literal_eval(legal.group(1))) if legal else 0
                    tags=e.get('speech',{}).get('acts',[])
                    if not isinstance(tags,list):reject('invalid_tag_field');continue
                    row=dict(run=run,seed=seed,event_index=idx,actor=actor,condition=log['auditor']['condition'],
                        auditor_active=int(status.group(1)=='ACTIVE'),turn=int(e['turn']),own_score=int(own.group(1)),
                        **{k:int(hand[k]) for k in ['wood','brick','sheep','wheat','ore']},listed_action_count=listed,
                        tagged_response=int(len(tags)>0),prompt_sha256=hashlib.sha256(p.encode()).hexdigest())
                    out.append(row)
    if len(seen)!=90:raise ValueError(f'Expected 90 games; got {len(seen)}')
    with (ROOT/'data/derived/surrogate_features.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    (ROOT/'results/surrogate_extraction.json').write_text(json.dumps({'rows':len(out),'runs':len(seen),'excluded':excluded,'input_features':FEATURES},indent=2))

def train():
    rows=list(csv.DictReader((ROOT/'data/derived/surrogate_features.csv').open()))
    x=np.array([[float(r[k]) for k in FEATURES] for r in rows]);y=np.array([int(r['tagged_response']) for r in rows]);groups=np.array([int(r['seed']) for r in rows])
    predictions=np.full(len(y),np.nan);baseline=np.full(len(y),np.nan);no_audit=np.full(len(y),np.nan)
    importance=[];folds=[]
    for fold,(tr,te) in enumerate(GroupKFold(n_splits=5).split(x,y,groups)):
        assert not set(groups[tr])&set(groups[te])
        model=DecisionTreeClassifier(max_depth=3,min_samples_leaf=250,random_state=20261123)
        model.fit(x[tr],y[tr]);predictions[te]=model.predict_proba(x[te])[:,1];baseline[te]=y[tr].mean()
        without=DecisionTreeClassifier(max_depth=3,min_samples_leaf=250,random_state=20261123)
        without.fit(x[tr,1:],y[tr]);no_audit[te]=without.predict_proba(x[te,1:])[:,1]
        imp=permutation_importance(model,x[te],y[te],scoring='roc_auc',n_repeats=10,random_state=20261123+fold,n_jobs=1)
        importance.append(imp.importances)
        folds.append({'fold':fold,'test_seeds':sorted(set(groups[te].tolist())),'test_rows':len(te),'auc':float(roc_auc_score(y[te],predictions[te]))})
    model=DecisionTreeClassifier(max_depth=3,min_samples_leaf=250,random_state=20261123).fit(x,y)
    tree=model.tree_;rules=[]
    def visit(node,parts):
        if tree.feature[node]<0:
            rules.append({'conditions':parts,'training_rows':int(tree.n_node_samples[node]),'tagged_probability':float(tree.value[node][0,1]/tree.value[node][0].sum())});return
        feature=FEATURES[tree.feature[node]];threshold=float(tree.threshold[node]);visit(tree.children_left[node],parts+[{'feature':feature,'operator':'<=','value':threshold}]);visit(tree.children_right[node],parts+[{'feature':feature,'operator':'>','value':threshold}])
    visit(0,[])
    imp=np.concatenate(importance,axis=1)
    result={'target':'Response supplies at least one speech-act tag in speech.acts; an imperfect checkability proxy, not truth',
        'method':'Depth-3 decision-tree surrogate plus held-out permutation feature importance',
        'status':'exploratory predictive associations, not causal effects or internal attributions',
        'rows':len(rows),'positive_rows':int(y.sum()),'tagged_share':float(y.mean()),'board_seeds':len(set(groups)),
        'cv':'Five folds holding out complete board seeds, including all repeated games and all conditions',
        'out_of_fold_auc':float(roc_auc_score(y,predictions)),'out_of_fold_ap':float(average_precision_score(y,predictions)),
        'out_of_fold_brier':float(brier_score_loss(y,predictions)),'baseline_brier':float(brier_score_loss(y,baseline)),
        'without_audit_feature_auc':float(roc_auc_score(y,no_audit)),
        'importance':[{'feature':f,'label':label,'mean_auc_drop':float(imp[i].mean()),'repeat_sd':float(imp[i].std())} for i,(f,label) in enumerate(zip(FEATURES,LABELS))],
        'folds':folds,'full_data_rules':rules,'full_tree_text':export_text(model,feature_names=FEATURES),
        'versions':{'numpy':np.__version__,'scikit_learn':sklearn.__version__},
        'limits':['Tag presence is an imperfect measure of checkability; tags may be invalid or action-bound and untagged speech may be checkable.','Surrogate has partial coverage of the information Qwen saw.','A feature absent from this tree is not established to be irrelevant to Qwen.','Permutation can produce unusual feature combinations.','Repeat SD is not a confidence interval.','Rows are dependent within games; predictive scores are descriptive.','No model tuning or causal inference is claimed.']}
    (ROOT/'results/communication_surrogate.json').write_text(json.dumps(result,indent=2))
    with (ROOT/'results/heldout_predictions.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['run','seed','event_index','tagged_response','heldout_probability']);w.writerows((r['run'],r['seed'],r['event_index'],int(t),float(p)) for r,t,p in zip(rows,y,predictions))
    print(json.dumps({k:v for k,v in result.items() if k not in ['full_data_rules','full_tree_text','folds','limits']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--archives');a=p.parse_args()
    if a.archives:extract(a.archives)
    train()
