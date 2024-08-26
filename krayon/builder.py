from ansi import Effect
from pathlib import Path

current_dir = Path(__file__).parent

with open(current_dir / 'generator/krayon.pre.py') as prefile:
    pre = prefile.read()

with open(current_dir / 'generator/krayon.template') as fnfile:
    fn = fnfile.read()


# removes top comment
pre = '"""'.join(pre.split('"""')[2:]) 


final = pre + '\n\n'

effects = [e for e in Effect.__dict__.keys() if '__' not in e]


for effect in effects:
    final += fn.format(c = effect.lower(), C = effect)

with open(current_dir / 'krayon.py', 'w') as finalfile:
    finalfile.write(final.strip())
