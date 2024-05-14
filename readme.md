# <span style="background:-webkit-linear-gradient(45deg, #0AF, #F00);-webkit-background-clip: text;-webkit-text-fill-color: transparent;">K R A Y O N: Python Terminal Colours</span>

The clean, lightweight, **zero-dependency**, cross-platform, ANSI escape code wrapper written in Python.

## Installation
Currently there is no PyPi Package for <span style="font-weight: 800;background:-webkit-linear-gradient(45deg, #0AF, #F00);-webkit-background-clip: text;-webkit-text-fill-color: transparent;">krayon.</span>

To use krayon the simplest way is to clone this repo
```bash
git clone github.com/enchanteddev/krayon
```
Then create a new ```.py``` file in the same folder as the ```krayon``` directory. A simple hello world would look like this:
```python
from krayon import C

print(C("Hello World!").red)
```
## Guide + Docs
### The C-string
The C string is the simplest method the style terminal output using ANSI codes. To create a C-string:
```python
from krayon import C

cstr = C("Hello") # this is a C-string
```
A C-string has a lot of options for styling it using chained methods (or "properties"). It also supports auto-completion in all IDEs/Text Editors that have auto-complete enabled.

**To style a C-string:**
```python
from krayon import C

red_cstr = C("Hello").red # this returns a C-string
red_with_bluebg_cstr = C("Hello").red.bg_blue # this returns a C-string
```

**Nested C-String**

C-strings can also handle nesting. When a C-string is inside another C-string it takes in the properties of the parent, while allowing overwriting any effects if needed.

```python
from krayon import C

nested_cstr = C(f'Hello {C("World").blue}').red.bg_cyan

# You can also do this without f-strings
nested_cstr = C('Hello ' + C("World").blue).red.bg_cyan

```

### Templates
An (opinionated) set of presets are given inside of templates, which can be used as follows:

```python
from krayon import templates as t

t.notify("Hello")
t.warning("Problem with line 4")
t.success("Task completed successfully")
```

You are free to make your own templates. The in-built templates makes the job easier by providing colour pre-sets out-of-the box.

The templates are as follows:

```python
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
```