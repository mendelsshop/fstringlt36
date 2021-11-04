def f(string):    
    output = ''
    var = ''
    next = False
    past_semicolon = False
    semicolon_value = ''
    for s in string:
        if s not in ['{','}'] and next != True and past_semicolon != True:
            output += s
        elif s == '{':
            next = True
        elif s == ':':
            past_semicolon = True
            next = False
        elif s == '}':
            past_semicolon = False
            # handle semicolon_value maybee use a function
            semicolon_value = semicolon_value.strip()
            print(semicolon_value)
            next = False
            exec('global var')
            # need to work on gloabal and local variables handling
            var = eval(var)
            output += var
            var = ''
        elif next == True:
            var += s
        elif past_semicolon == True:
            semicolon_value += s
    # handle padding
    return output
def main():
    global hello, world
    hello = "Hello,"
    world = "world" 
    string = '{hello} {world:  5556  }'
    print(f(string))

if __name__ == '__main__':
    main()


