"""
Templates for the krayon library.
Use this as an alternative to 'input' and 'print'.
"""

from .krayon import C

def input_(string) -> str:
    print(string, end='')
    return input()

ask = lambda x: input_(C(x).bright_magenta)
status = lambda x: print(C(x).cyan)
warning = lambda x: print(C(x).red)
success = lambda x: print(C(f'✓ {x}').bright_green)
error = lambda x: print(C(f'✘ {x}').red)
notify = lambda x: print(C(x).bright_blue)
confirm = lambda x: input_(C('? ' + f'{x} (y/n) ').white).lower() == 'y'


def main():
    notify('You said: ' + ask('HI! whats your name?'))
    status('This workin fine.')
    warning('This scary?')
    success('Then this was a success')
    error('Stoopid hooman detected!!')
    notify('Erasing stoopid hooman')
    status('Deleting Hooman' * confirm('Confirm erasing hooman'))



if __name__ == '__main__':
    main()