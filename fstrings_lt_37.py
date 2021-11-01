def f(string):    
    output = ''
    var = ''
    for s in string:
        if s not in ['{','}'] and _coninue != True:
            output += s
        elif s == '{':
            _coninue = True
        elif s == '}':
            _coninue = False
            exec('global var')
            # need to work on gloabal and local variables handling
            var = eval(var)
            output += var
            var = ''
        elif _coninue == True:
            var += s
    # handle padding
    return output
def main():
    global hello, world
    hello = "Hello,"
    world = "world" 
    string = '{hello} {world}'
    print(f(string))

if __name__ == '__main__':
    main()


