from ansi import Effect


with open('generator/pastel.pre.py') as prefile:
    pre = prefile.read()

with open('generator/pastel.template') as fnfile:
    fn = fnfile.read()

final = pre + '\n\n'

effects = [e for e in Effect.__dict__.keys() if '__' not in e]


for effect in effects:
    final += fn.replace('{c}', effect.lower()).replace('{C}', effect)

with open('pastel.py', 'w') as finalfile:
    finalfile.write(final)
