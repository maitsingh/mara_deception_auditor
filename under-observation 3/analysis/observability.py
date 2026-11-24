"""Inventory evidence retained in existing H5 archives; makes no inference calls."""
import argparse, collections, csv, hashlib, json, re, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SETTING_KEYS={'temperature','top_p','top_k','max_tokens','max_output_tokens','enable_thinking','thinking','reasoning_effort','checkpoint','revision'}
CHANNEL_KEYS={'reasoning_content','reasoning','hidden_states','activations','attention','logprobs','token_logprobs'}
def inventory(folder):
    manifest=json.loads((ROOT/'data/source/archive_manifest.json').read_text())
    counts=collections.Counter();models=collections.Counter();settings=collections.defaultdict(set);channels=collections.Counter();raw_keys=collections.Counter();runs=set();marker_examples=[]
    def walk(obj):
        if isinstance(obj,dict):
            for key,value in obj.items():
                if key in SETTING_KEYS:settings[key].add(json.dumps(value,sort_keys=True))
                walk(value)
        elif isinstance(obj,list):
            for value in obj:walk(value)
    for entry in manifest:
        path=Path(folder)/entry['original_filename']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256']
        with zipfile.ZipFile(path) as archive:
            meta=json.loads(archive.read('experiment.json'))
            for run in meta['runs']:
                cfg=run.get('config',{})
                if isinstance(cfg,str):cfg=json.loads(cfg)
                walk(cfg)
            for name in archive.namelist():
                if not(name.startswith('logs/') and name.endswith('.json')):continue
                run=int(re.search(r'_run(\d+)_',name).group(1));assert run not in runs;runs.add(run)
                log=json.loads(archive.read(name))
                for event in log['events']:
                    if not event.get('prompt') or event.get('turn',0)<1 or event.get('type')=='rejected_ask':continue
                    counts['post_setup_prompted_events']+=1
                    for field in ['prompt','raw','private','public','stamp','speech','usage']:
                        if event.get(field) is not None:counts['with_'+field]+=1
                    usage=event.get('usage') or {}
                    if usage.get('model'):models[str(usage['model'])]+=1
                    for key in CHANNEL_KEYS:
                        if key in event or key in usage:channels[key]+=1
                    raw=event.get('raw')
                    if isinstance(raw,str):
                        if '<think>' in raw or '</think>' in raw:
                            counts['raw_with_think_delimiter']+=1
                            marker_examples.append({'run_id':run,'event_index_zero_based':log['events'].index(event),'turn':event.get('turn'),'actor':event.get('actor') or event.get('proposer') or event.get('responder'),'raw_sha256':hashlib.sha256(raw.encode()).hexdigest(),'source_archive':entry['original_filename']})
                        try:parsed=json.loads(raw)
                        except (ValueError,TypeError):parsed=None
                        if isinstance(parsed,dict):
                            raw_keys.update(parsed.keys())
                            for key in CHANNEL_KEYS:
                                if key in parsed:channels['raw.'+key]+=1
    metrics=list(csv.DictReader((ROOT/'data/source/game_metrics.csv').open()))
    false=[int(row['hand_statements_false_before'])+int(row['hand_statements_false_after']) for row in metrics]
    result={'status':'Inventory of retained export fields, not a test of internal awareness or scorer validity','runs':len(runs),'event_fields':dict(counts),'usage_model_counts':dict(models),'generation_settings_found':{k:sorted(v) for k,v in settings.items()},'separate_channel_keys_found':dict(channels),'raw_json_keys':dict(raw_keys),'reasoning_delimiter_examples':marker_examples,'own_resource_false_claims':{'total':sum(false),'games_with_zero':false.count(0),'games_with_at_least_one':sum(x>0 for x in false),'maximum_per_game':max(false)},'interpretation':['Missing export fields do not establish that a provider or model lacks those capabilities.','private_reasoning is a generated application-level JSON field, not certified native reasoning or an activation trace.','No native thinking-mode setting should be inferred from the absence of think delimiters.']}
    assert len(runs)==90
    return result
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--archives',required=True);args=ap.parse_args();result=inventory(args.archives);out=ROOT/'results/observability_inventory.json';out.write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
