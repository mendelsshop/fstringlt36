timem = 0
def var_handle(var): # -> str
    global timem
    exec('global var')
    # need to work on gloabal and local variables handling
    try:
        var = eval(var)

    except SyntaxError:
        pass

    return var


def f(string): # -> str
    global timem
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
            var = var_handle(var)
            
            continue

        elif s == '}':
            next = False

            if past_semicolon == True:
                past_semicolon = False

                if semicolon_value:

                    if semicolon_value[0] in ['<', '>']:

                        if semicolon_value[0] == '<':
                            semicolon_value = semicolon_value.strip('< ')
                            print(semicolon_value)

                        elif semicolon_value[0] == '>':
                            semicolon_value = semicolon_value.strip('> ')
                            print(semicolon_value)
            
            elif past_semicolon == False:
                var = var_handle(var)

            output += var
            var = ''
            semicolon_value = ''

        elif next == True:
            var += s
            
        if past_semicolon == True:
            semicolon_value += s

    # handle padding
    return output


def main(): # -> none
    global hello, world
    hello = "Hello,"
    world = "world" 
    string = '{hello} {world: < {5556}  }'
    print(f(string))


if __name__ == '__main__':
    main()




