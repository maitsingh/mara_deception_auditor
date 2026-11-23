"""Reproduce the numerical analyses and website from included data. No API calls."""
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
for script in ['analysis/behavior.py','analysis/communication.py','scripts/build_site.py']:
    print(f'Running {script}',flush=True)
    subprocess.run([sys.executable,str(ROOT/script)],check=True,cwd=ROOT)
print('Results are in results/. Open site/index.html to view the rebuilt project.')
