"""Build the standalone research site from supplied metrics and source extracts."""
import csv
import base64
import json
import shutil
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'analysis'))
from behavior import analyze

def build():
    metrics=list(csv.DictReader((ROOT/'data/source/game_metrics.csv').open()))
    records=json.loads((ROOT/'data/source/decision_contexts.json').read_text())
    notes=list(csv.DictReader((ROOT/'data/source/auditor_notes_source.csv').open()))
    return render(metrics,records,notes)

def render(metrics, records, notes):
    result = analyze()
    (ROOT/'results/behavior.json').write_text(json.dumps(result, indent=2))
    # Source records remain immutable during a site build.
    payload = {'games':metrics, 'notes':records, 'analysis':result,
        'surrogate':json.loads((ROOT/'results/communication_surrogate.json').read_text()),
        'surrogate_extraction':json.loads((ROOT/'results/surrogate_extraction.json').read_text()),
        'source_category_counts':dict(Counter(r['stated_response'] for r in notes)),
        'observability':json.loads((ROOT/'results/observability_inventory.json').read_text())}
    image='data:image/png;base64,'+base64.b64encode((ROOT/'site/assets/catanist-interface.png').read_bytes()).decode()
    logo='data:image/png;base64,'+base64.b64encode((ROOT/'site/assets/trust-lab-logo.png').read_bytes()).decode()
    fonts=[]
    for file,family,weight,style in [
        ('LiberationSans-Regular.ttf','Observation Sans',400,'normal'),
        ('LiberationSans-Bold.ttf','Observation Sans',700,'normal'),
        ('LiberationSerif-Regular.ttf','Observation Serif',400,'normal'),
        ('LiberationSerif-Bold.ttf','Observation Serif',700,'normal'),
        ('LiberationSerif-Italic.ttf','Observation Serif',400,'italic')]:
        encoded=base64.b64encode((ROOT/'site/assets/fonts'/file).read_bytes()).decode()
        fonts.append(f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};font-display:swap;src:url(data:font/ttf;base64,{encoded}) format('truetype')}}")
    html = (ROOT/'site/template.html').read_text().replace('__GAME_IMAGE__',image).replace('__TRUST_LOGO__',logo).replace('__EMBEDDED_FONTS__','\n'.join(fonts)).replace('__RESEARCH_DATA__', json.dumps(payload, ensure_ascii=False).replace('</', '<\\/'))
    (ROOT/'site/index.html').write_text(html)
    print(json.dumps({'games':len(metrics),'notes':len(records),'html_bytes':len(html.encode())}))

if __name__ == '__main__': build()
