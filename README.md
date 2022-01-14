# f-string_lt_37 Regex Edition
## About: 
Python f-strings for before Python 3.7. using Regex
<br>
This package should try to emulate all f-string features <br>by using a class that inherits from str.
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

### basic string replacement

```python
>>> from f_string_lt_37 import f
>>> hello = "Hello,"
>>> f("{hello} world")
'hello world'
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
>>> from fstring_lt_37 import f
>>> var = 'foo'
>>> s = f("{var}")
>>> print(s)
'foo'
>>> t = s.f_string_parse()
>>> print(t)
'error: variable value not found'
>>> print(s)
'error: variable value not found'
# besides for messing up t it will also mess up s because it's a reference to the same object.

```
## Version: 
Version Number: 0.0.2
<br>
Version Stage: alpha

