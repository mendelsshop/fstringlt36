def f(string):    
    output = ''
    var = ''
    next = False
    past_semicolon = False
    semicolon_value = ''
    for s in string:
        # make 2 semilcon indicators for semicolon stepping
        if s not in ['{','}',':'] and next != True and past_semicolon != True:
            
            output += s
        elif s == '{':
            if past_semicolon:
                next = False
            else:
                next = True

        elif s == ':':
            past_semicolon = True
            next = False
        
        elif s == '}':
            
            past_semicolon = False
            next = False
            # handle semicolon_value maybee use a function
            semicolon_value = semicolon_value.strip()
            if semicolon_value:
                if semicolon_value[0] in ['<', '>']:
                    if semicolon_value[0] == '<':
                        semicolon_value = semicolon_value.strip('< ')
                        semicolon_value = semicolon_value.strip('{}')
                        print(semicolon_value)
                    elif semicolon_value[0] == '>':
                        semicolon_value = semicolon_value.strip('> ')
                        semicolon_value = semicolon_value.strip('{}')
                        print(semicolon_value)
            
            exec('global var')
            # need to work on gloabal and local variables handling
            var = eval(var)
            output += var
            var = ''
            semicolon_value = ''
        elif past_semicolon == True:
            semicolon_value += s
        elif next == True:
            var += s

    # handle padding
    return output
def main():
    global hello, world
    hello = "Hello,"
    world = "world" 
    string = '{hello} {world: < {5556}  }'
    print(f(string))

if __name__ == '__main__':
    main()




