[![tests](https://github.com/mendelsshop/fstringlt36/actions/workflows/test.yml/badge.svg?branch=regex)](https://github.com/mendelsshop/fstringlt36/actions/workflows/test.yml)
[![flake8](https://github.com/mendelsshop/fstringlt36/actions/workflows/flake8.yml/badge.svg)](https://github.com/mendelsshop/fstringlt36/actions/workflows/flake8.yml)
[![Upload Python Package](https://github.com/mendelsshop/fstringlt36/actions/workflows/python-publish.yml/badge.svg)](https://github.com/mendelsshop/fstringlt36/actions/workflows/python-publish.yml)
# fstringlt36 Regex Edition
## Installation: pip install fstringlt36
## About: 
Python f-strings for before Python 3.6. using Regex
<br>
This package should try to emulate all f-string features <br>by using a class that inherits from str.
<br>
You can also use it to get newer f-string features in earlier versions of Python.
<br>
such as: `h = 'hello'; f'{h = }'`. the ; is just to denonote the end of a line.
<br>
This package requires the re (regular expressions, regex) module.
<br>
To my knowledge most versions of Python have re, if not you can use the non regex version
<br>
So it should be able to install on any Python version.
<br>
Although it's not been tested if thats true because it's not working yet.
<br>
Once I implement all the features I will test it across multiple python version and platforms.
<br>

## Features currently working:

### basic variable replacement

```python
>>> from fstringlt36 import f
>>> h = "Hello,"
>>> f("{h} world")
hello world
```
#### using the equal operator (I don't know a better name for this and I'm to lazy to look at the document)
```python
>>> from fstringlt36 import f
>>> h = "Hello,"
>>> # instead of doing print(f("h = {h}"))
>>> # you can do print(f("{h = }"))
>>> print(f("{h = }"))
h = 'Hello,'
```
#### note:
please note to not call `f().f_string_parse()` directly but use the `f()` class.
<br>
if you try to `f_string_parse()` to use directly it will ruin your output and fall back to:

```python
>>> value = 'error: variable ' + string + ' not found'
```

where value is the replacement string to whatever you put in `{}`.

```python
>>> from fstringlt36 import f
>>> var = 'foo'
>>> s = f("{var}")
>>> print(s)
foo
>>> t = s.f_string_parse()
>>> print(t)
error: variable value not found
>>> print(s)
error: variable value not found
# besides for messing up t it will also mess up s because it's a reference to the same object.

```
## Version: 
Version Number: 0.0.3
<br>
Version Stage: alpha

