# f-string_lt_37
## About: 
Python f-strings for before Python 3.7.
<br>
This package should try to emulate all f-string features <br>by using a class that inherits from str.
<br>
This package shouldn't require any other packages.
<br>
So it should be able to install on any Python version.
<br>
Although it's not been tested if thats true because it's not working yet.
<br>
## Features currently working:
### !a and !r  for assci() and repr().

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
### Multiple curly/sciggly braces to output 1 or more curly/sciggly braces now works.
```
import fstring_lt_37.f

h = 'hello'

# using negative amounts of {} 
# results in evaluating whats in the {}
print(f('{{{h}}}'))

# result = {hello}

# using posotive amounts of {} 
# results in not  evaluating whats in the {}
# so in the example below we end up with h 
# because python does not evaluate the var
print(f('{{h}}'))

# result = {h}
```
## Version: 
Version Number: 0.0.3
<br>
Version Stage: alpha

