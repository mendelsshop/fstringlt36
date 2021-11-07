#combine var_handle and f to make a function that can handle all the var stuff
class f(str):
    def __init__(self, string):
        self.string = string
    def var_handle(self,var): # -> str
        # need to work on gloabal and local variables handling
        try:
            var = eval(var)

        except SyntaxError:
            pass
 
        return var
    def change_to_fstring(self):
        output = ''
        var = ''
        next = False
        past_semicolon = False
        past_padding = False
        semicolon_value = ''
        for s in self.string:
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
                var = self.var_handle(var)
            
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
                    var = self.var_handle(var)

                output += var
            
                var = ''
                semicolon_value = ''

            elif next == True:
                var += s
            
            if past_semicolon == True:
                semicolon_value += s

        # handle padding

        return output
    def __repr__(self):
        return self.change_to_fstring()
    def __str__(self):
        return self.change_to_fstring()

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

    string = '{hello} {world:>11}hiyyy'
    string1 = f'{hello} {world:>13}hiyyy'

    
    print(len(f(string)))
    print(repr(f(string)))
    print(len(string1))
    print(repr(string1))


if __name__ == '__main__':
    main()
