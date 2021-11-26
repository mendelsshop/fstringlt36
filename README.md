# f-string_lt_37
## About: 
Python f-strings for before Python 3.7.
<br>
This package shouldn't require any other packages.
<br>
So it should be able to install on any Python version.
<br>
Although it's not been tested if thats true because it's not working yet.
<br>
## Features currently working:
!a and !r are curently working.
<br>
```
import fstring_lt_37.f

h = 'hello'

# !a calls ascii()

print(f('!a =  {h!a}'))

# result of !a =  'hello'

# !r calls repr()

print(f('!r =  {h!r}'))

# result of !r =  'hello' 
```
using multiple curly/sciggly braces to output 1 or more curly/sciggly braces now works
```
import fstring_lt_37.f

h = 'hello'

# from what I tested so far in Python3.9.9
# you need to use add 2 more {{ not just one 
# but if not the case its very easy to fix

print(f('{{{h}}'))

# result = {hello}
```
## Version: 
Version-Number: 0.0.3
<br>
Version-Stage: alpha

