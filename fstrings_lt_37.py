def f(string):    
    output = ''
    var = ''
    next = False
    past_semicolon = False
    past_padding = False
    semicolon_value = ''
    for s in string:
        # make 2 semilcon indicators for semicolon stepping
        if s not in ['{','}',':'] and next != True and past_semicolon != True and  past_padding != True:
            output += s
        elif s == '{':
            if past_semicolon:
                next = False
                continue
            else:
                next = True

        elif s == ':':
            past_semicolon = True
            next = False
            # handle var so turn var handling into a function
            
            continue

        elif s == '}':
            if past_semicolon:
                past_semicolon = False
                if semicolon_value:
                    if semicolon_value[0] in ['<', '>']:
                        if semicolon_value[0] == '<':
                            semicolon_value = semicolon_value.strip('< ')
                            print(semicolon_value)
                        elif semicolon_value[0] == '>':
                            semicolon_value = semicolon_value.strip('> ')
                            print(semicolon_value)
            
            
            next = False

            exec('global var')
            # need to work on gloabal and local variables handling
            print(var)
            var = eval(var)
            output += var
            var = ''
            semicolon_value = ''
        elif next == True:
            var += s
            
        if past_semicolon == True:
            
            semicolon_value += s


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




