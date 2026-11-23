import csv, json, unittest, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read_csv(name):
 with (ROOT/name).open() as f:return list(csv.DictReader(f))
class ResearchChecks(unittest.TestCase):
 def test_behavioral_totals(self):
  rows=read_csv('data/source/game_metrics.csv')
  self.assertEqual(len(rows),90)
  self.assertEqual(sum(int(r['hand_statements_false_'+p]) for r in rows for p in ['before','after']),75)
  self.assertEqual(sum(int(r['hand_statements_checked_'+p]) for r in rows for p in ['before','after']),5650)
 def test_exact_contexts(self):
  rows=json.loads((ROOT/'data/source/decision_contexts.json').read_text())
  self.assertEqual(len(rows),96)
  for r in rows:
   d=r['source_record']
   self.assertEqual(hashlib.sha256(d['prompt'].encode()).hexdigest(),d['prompt_sha256'])
   self.assertEqual(hashlib.sha256(d['system_prompt'].encode()).hexdigest(),d['system_sha256'])
 def test_surrogate_heldout_seeds(self):
  d=json.loads((ROOT/'results/communication_surrogate.json').read_text())
  seeds=[seed for f in d['folds'] for seed in f['test_seeds']]
  self.assertEqual(len(seeds),20)
  self.assertEqual(len(set(seeds)),20)
  self.assertEqual(sum(f['test_rows'] for f in d['folds']),d['rows'])
  preds=read_csv('results/heldout_predictions.csv')
  self.assertEqual(len(preds),29147)
  self.assertTrue(all(0<=float(r['heldout_probability'])<=1 for r in preds))
 def test_surrogate_features(self):
  rows=read_csv('data/derived/surrogate_features.csv')
  self.assertEqual(len(rows),29147)
  self.assertEqual(sum(int(r['tagged_response']) for r in rows),8746)
  self.assertNotIn('private',rows[0])
  self.assertEqual(len({(r['run'],r['event_index']) for r in rows}),len(rows))
 def test_site_and_poster(self):
  s=(ROOT/'site/index.html').read_text()
  self.assertNotIn('__GAME_IMAGE__',s)
  self.assertNotIn('id="responsibility"',s)
  self.assertIn('id="awareness"',s)
  self.assertIn('data:image/png;base64,',s)
  self.assertIn('Duke University',s)
  self.assertIn('Project lead: Shreya Mendi',s)
  self.assertIn('Audit design and accountability for orchestrators',s)
  self.assertNotIn('__EMBEDDED_FONTS__',s)
  self.assertNotIn('__DUKE_LOGO__',s)
  self.assertIn('Observation Sans',s)
  self.assertIn('width="24in" height="32in"',(ROOT/'poster/Under_Observation_Poster_24x32.svg').read_text()[:200])
if __name__=='__main__':unittest.main()
