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
    # need to work on padding size config compared to real fstrings
    global timem
    output = ''
    var = ''
    next = False
    past_semicolon = False
    past_padding = False
    semicolon_value = ''
    for s in string:
        # make 2 semilcon indicators for semicolon stepping
        # print(len(output))
        # print(output+'t')
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
                            space = ' ' * int(semicolon_value)
                            
                            var = var + space

                        elif semicolon_value[0] == '>':
                            semicolon_value = semicolon_value.strip('> ')
                            
                            space = ' ' * int(semicolon_value)
                            
                            var =  space + var
            
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
    # print(output)
    return output


def main(): # -> none
    global hello, world
    hello = "Hello,"
    world = "world" 
    string = '{hello} {world:<8}hiyyy'
    string1 = f'{hello} {world:<13}hiyyy'
    # block = ''
    # block = f'{block:<10}'
    # print(len(block))
    # print(len(f(string)))
    # print(len(string1))
    # print(string1)
    # 8 = 13
    # figure out diifreence n padding

    string = '{hello} {world:>8}hiyyy'
    string1 = f'{hello} {world:>13}hiyyy'

    
    print(len(f(string)))
    print(f(string))
    print(len(string1))
    print(string1)

if __name__ == '__main__':
    main()




