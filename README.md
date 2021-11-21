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
!a and !r are curently working.
<br>
```
import fstring_lt_37.f

h = 'hello'

# !a calls ascii()

print(f('!a =  {h!a}'))

# result = !a =  'hello'

# !r calls repr()

print(f('!r =  {h!r}'))

# result = !r =  'hello' 
```
## Version: 
Version-Number: 0.0.2
<br>
Version-Stage: alpha

