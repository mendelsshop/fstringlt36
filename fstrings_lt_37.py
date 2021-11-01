def f(string):
    
    # string = '{hello} world'
    output = ''
    var = ''
    for s in string:
        if s not in ['{','}'] and _coninue != True:
            output += s
  
        elif s == '{':
            _coninue = True
        elif s == '}':
            _coninue = False
            var = eval("hello")
            print(var)
            output += var
        elif _coninue == True:
            var += s
    return output
hello = "Hello,"
string = '{hello} world'
print(f(string))

