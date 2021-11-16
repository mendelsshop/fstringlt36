import logging
logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
# fix spagghetti code in f class 
def boxify(list):
    # find larggest string in list
    larggest_string = len(max(list, key=len))
    print('#' *(larggest_string+4))
    for item in list:
        # center each item with .center(larggest_string)
        print('#',item.center(larggest_string), '#')
    print('#' *(larggest_string+4))
    
        

class f(str):
    def __init__(self, string) -> None:
        self.string = string
        self.version = '0.0.1-alpha'
        logging.info('Started')

        
    def phase_change(self, phase) -> None:
        self.current_phase = phase

        logging.info('changing to ' + phase)
        return None
    def var_handle(self,var) -> str:
        # need to work on gloabal and local variables handling
        try:
            exec('global var')
            var = eval(var)

        except SyntaxError:
            print('error: variable')
            pass
 
        return var
    def f_string_parse(self) -> str:
        self.current_phase = 'parsing'
        self.i = 0
        self.output = ''
        self.var_handling = True
        self.var = ''
        self.dummy_var = ''

        def info():
            try:
                self.string[self.i]
            except IndexError:
                return False
            # logging.info('f string parser version: ' + self.version)
            if self.current_phase:
                logging.info('current phase: ' + self.current_phase)
            if self.string[self.i]:
                logging.info('current substring: ' + self.string[self.i])
            if self.var:
                logging.info('var: ' + self.var)
            if self.output:
                logging.info('output: ' + self.output)
            logging.info('var handling: ' + str(self.var_handling))
            # logging.info('dummy_var', self.dummy_var)
            return None        

        while len(self.string) > self.i:
            logging.info('================================================================')
            # for self.i in range(len(self.string)):       
            if self.current_phase == 'parsing':
                if self.string[self.i] == '{':
                    self.phase_change('f_string')
                    self.i += 1
                    info()
                    logging.info('changing to f_string parsing')
                      
                else:
                    self.output += self.string[self.i]
                    self.i += 1
                    info()
                    logging.info('adding to output')
                   
            elif self.current_phase == 'f_string':
                if self.string[self.i] in  ['\"','\''] and self.var_handling == True: 
                    self.var_handling = False
                    self.var += self.string[self.i]
                    self.i += 1
                    info()
                    logging.info('adding to var without var handling')
                   
                elif self.string[self.i] in ['\'','\"'] and self.var_handling == False:
                    self.var_handling = True
                    self.i += 1
                    info()
                    logging.info('stop adding to var with var handling')
                   
                elif self.string[self.i] == '}' and self.var_handling == True:
                    self.phase_change('parsing')
                    if self.var[0] in ['\'','\"']:
                        self.var = self.var.strip('\"\'')
                    else:
                        self.var = self.var_handle(self.var)
                    if len(self.string) > self.i:
                        self.i += 1
                        self.output += self.var
                        self.var = ''
                    else:
                        self.output += self.var
                        self.var = ''
                        self.i += 1
                    logging.info('adding var to output')
                    
                   
                elif self.string[self.i] == ':' and self.var_handling == True:
                    self.phase_change('after f_string')
                    self.i += 1
                    info()
                    logging.info('changing to after f_string parsing')
                   
                else:
                    self.var += self.string[self.i]
                    logging.info('adding to var'+self.string[self.i] +' with var handling')
                    self.i += 1  
                    info()
                   

            elif self.current_phase == 'after f_string':
                if self.string[self.i] == '}':
                    self.phase_change('f_string')
                    info()
                    logging.info('changing to f_string parsing')
                else:
                    if self.string[self.i] in ['<','>']:
                        pass
                    self.dummy_var += self.string[self.i]
                    self.i += 1

                    info()
                    logging.info('handling padding')
        logging.info('Done')
        return self.output
        


    def __repr__(self) -> str:
        return '\'' + self.f_string_parse() + '\''
    def __str__(self) -> str:
        return self.f_string_parse()

def main() -> None:
    global hello, world
    hello = "Hello,"
    world = "wo" 
    string = f('{hello} {world}hiyyy')
    string1 = f'{hello} {world}hiyyy'
    tests = []
    tests.append('len of fake f_string ' + str(len(string)))
    # need to work on calling f_string.f from another variable
    tests.append('fake f_string ' + f(string))
    tests.append('len of real f_string ' + str(len(string1)))
    tests.append('real f_string ' + string1)
    boxify(tests)
    # need to fix type


if __name__ == '__main__':
    main()
