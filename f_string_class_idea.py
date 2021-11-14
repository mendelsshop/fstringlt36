#combine var_handle and f to make a function that can handle all the var stuff
# fix spagghetti code in f class 


# make multi level if elses
# if found_ariable
# if past_semicolon
# etc


class f(str):
    def __init__(self, string) -> None:
        self.string = string
    def var_handle(self,var) -> str:
        # need to work on gloabal and local variables handling
        
        try:
            exec('global var')
            var = eval(var)

        except SyntaxError:
            print('error: variable')
            pass
 
        return var
    def change_to_fstring(self) -> str:
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
                # print('done')
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
                                space = ' ' * (len(var) - int(semicolon_value))
                                print(len(space))
                                var = var + space

                            elif semicolon_value[0] == '>':
                                semicolon_value = semicolon_value.strip('> ')
                            
                                space = ' ' * (len(var) - int(semicolon_value))
                                print(len(space))
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

    def __repr__(self) -> str:
        return self.change_to_fstring()
    def __str__(self) -> str:
        return self.change_to_fstring()

def main() -> None:
    global hello, world
    hello = "Hello,"
    world = "wo" 
    # string = '{hello} {world:<8}hiyyy'
    # string1 = f'{hello} {world:<13}hiyyy'


    string = f('{hello} {world:>5}hiyyy')
    string1 = f'{hello} {world:>5}hiyyy'

    
    print(len(string))
    print(string)
    print(string)
    print(len(string1))
    print(string1)
    # need to fix type
    # print(type(string)) 
    # print(type(f'{"hello"}'))


if __name__ == '__main__':
    main()
