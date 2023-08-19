# <span style="background:-webkit-linear-gradient(45deg, #0AF, #F00);-webkit-background-clip: text;-webkit-text-fill-color: transparent;">P A S T E L: Python Terminal Colours</span>

The clean, lightweight, **zero-dependency**, cross-platform, ANSI escape code wrapper written in Python.

## Installation
Currently there is no PyPi Package for <span style="font-weight: 800;background:-webkit-linear-gradient(45deg, #0AF, #F00);-webkit-background-clip: text;-webkit-text-fill-color: transparent;">PASTEL.</span>

To use pastel the simplest way is to clone this repo
```bash
git clone github.com/enchanteddev/Pastel
```
Then create a new ```.py``` file in the same folder as the ```pastel``` directory. A simple hello world would look like this:
```python
from pastel import C

print(C("Hello World!").red)
```
Output: <span style="color:red">Hello World!</span>

## Guide + Docs
### The C-string
The C string is the simplest method the style terminal output using ANSI codes. To create a C-string:
```python
from pastel import C

cstr = C("Hello") # this is a C-string
```
A C-string has a lot of options for styling it using chained methods (or "properties"). It also supports auto-completion in all IDEs/Text Editors that have auto-complete enabled.

**To style a C-string:**
```python
from pastel import C

red_cstr = C("Hello").red # this returns a C-string
```
🚧🚧🚧

**<span style="color:red">Incomplete Documentation!</span>**

🚧🚧🚧