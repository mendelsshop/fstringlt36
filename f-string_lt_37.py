#!/usr/bin/env python3
from ensurepip import version
import logging
#should probably do a better job for logging
logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
# fix spagghetti code in f class 
def boxify(list):
    '''
    the boxify function is just way to test results in a nice boxify function
    first we find the larggest string in the list given to the boxify function
    then we print a hash/number sign times longest string + 4
    then we go through each iem in the list and print a hash/number sign than using the str.center() method we center the current string by the largest string
    followed by another hash/number sign
    than we again do the hash/number sign times longest string + 4
    '''
    # find larggest string in list
    larggest_string = len(max(list, key=len))
    print('#' *(larggest_string+4))
    for item in list:
        # center each item with .center(larggest_string)
        print('#',item.center(larggest_string), '#')
    print('#' *(larggest_string+4))
    

class f(str):
    def __init__(self, string) -> None:
        # dummy_var is just for catching whatever doesnt work so far like {{}}
        self.string = string
        self.version = '0.0.3-alpha'
        self.current_phase = 'parsing'
        self.i = 0
        self.output = ''
        self.var_handling = True
        self.var = ''
        self.change_to = ''
        self.dummy_var = ''
        self.is_in_lt_or_gt = False
        self.should_be_padding = False
        self.amount_of_curly_braces = 0
        logging.info('Started')

    def phase_change(self, phase) -> None:
        '''
        this method if for changing the phase of the f class parsing
        the reason that it's in a method is because its easier to log/print in one place
        '''
        self.current_phase = phase
        logging.info('changing to ' + phase)
        return None

    def info(self) -> None:
        try:
            self.string[self.i]
        except IndexError:
            return False
        # logging.info('f string parser version: ' + self.version)
        logging.info('version: ' + self.version)
        if self.current_phase:
            logging.info('current phase: ' + self.current_phase)

        if self.string[self.i]:
            logging.info('current substring: ' + self.string[self.i])
            
        if self.var:
            logging.info('var: ' + self.var)
            
        if self.output:
            logging.info('output: ' + self.output)

        if self.dummy_var:
            logging.info('dummy_var: ' + self.dummy_var)
        # logging.info('var handling: ' + str(self.var_handling))
        # logging.info('dummy_var', self.dummy_var)
        return None        

    def var_handle(self) -> None:
        # need to work on gloabal and local variables handling
        try:
            try:
                exec('global var')
            except:
                logging.info('global var not defined')
            self.var = eval(self.var)
        except NameError:
            logging.error('error: variable name not found')
            self.var = 'error: variable name not found'
        except SyntaxError:
            logging.error('error: variable')
            self.var = 'error: variable'

    def f_string_parse(self) -> str:
        while len(self.string) > self.i:
            logging.info('================================================================')
            # for self.i in range(len(self.string)):       
            if self.current_phase == 'parsing':
                if self.string[self.i] == '{':
                    self.phase_change('f_string')
                    self.i += 1
                    self.info()
                    logging.info('changing to f_string parsing')
                      
                else:
                    self.output += self.string[self.i]
                    self.i += 1
                    self.info()
                    logging.info('adding to output')
                   
            elif self.current_phase == 'f_string':
                if self.string[self.i] in  ['\"','\''] and self.var_handling is True: 
                    self.var_handling = False
                    self.var += self.string[self.i]
                    self.i += 1
                    self.info()
                    logging.info('adding to var without var handling')
                   
                elif self.string[self.i] in ['\'','\"'] and self.var_handling is False:
                    self.var_handling = True
                    self.i += 1
                    self.info()
                    logging.info('stop adding to var with var handling')
                elif self.string[self.i] == '{':
                    self.amount_of_curly_braces += 1
                    self.i += 1
                   
                elif self.string[self.i] == '}' and self.var_handling is True:
                    self.phase_change('parsing')
                    if self.var[0] in ['\'','\"']:
                        self.var = self.var.strip('\"\'')

                    else:
                        self.var_handle()
                    self.i += 1
                    if self.change_to in ['r','a']:
                        if self.change_to == 'r':
                            self.var = repr(self.var)

                        elif self.change_to == 'a':
                            # return ascci of var
                            self.var = ascii(self.var)
                    if self.amount_of_curly_braces > 1:
                        self.var = self.curly_bracealize(self.var)
                        self.i += self.amount_of_curly_braces 
                    self.change_to = ''
                    self.output += self.var
                    self.var = ''
                    self.dummy_var = ''
                    self.is_in_lt_or_gt = False
                    self.should_be_padding = False
                    self.current_phase = 'parsing'
                    self.var_handling = True
                    self.amount_of_curly_braces = 0
                    logging.info('adding var to output')
                   
                elif (self.string[self.i] == ':' or self.string[self.i] == '!') and self.var_handling is True:
                    # probably shouldn't need to go after f_string parsing if ! and just do it here
                    self.phase_change('after f_string')
                    self.i += 1
                    self.info()
                    logging.info('changing to after f_string parsing')
                   
                else:
                    # need to work on '/" for dictionary keys beause it not adding the end quote
                    self.var += self.string[self.i]
                    logging.info('adding to var '+self.string[self.i] +' with var handling')
                    self.i += 1  
                    self.info()
                   
            elif self.current_phase == 'after f_string':
                if self.string[self.i] == '}':
                    self.phase_change('f_string')
                    self.info()
                    self.var_handling = True
                    logging.info('changing to f_string parsing')
                    continue

                elif self.string[self.i-1 ] + self.string[self.i] == '!s':                       
                    self.i += 1
                    self.info()

                elif self.string[self.i-1 ] + self.string[self.i] == '!r':
                    self.change_to = 'r'
                    self.i += 1
                    self.info()
                
                elif self.string[self.i-1 ] + self.string[self.i] == '!a':
                    self.change_to = 'a'
                    self.i += 1
                    self.info()

                elif self.string[self.i] in ['<','>']:
                    self.is_in_lt_or_gt = True
                    if self.string[self.i] == '<':
                        self.should_be_padding = 'left aligned'
                    
                    elif self.string[self.i] == '>':
                        self.should_be_padding = 'right aligned'
                    self.i += 1
                    self.info()
                else:
                    self.dummy_var += self.string[self.i]
                    self.i += 1
                    self.info()
                    logging.info('handling padding')
        logging.info('Done')
        return self.output
    def curly_bracealize(self,string) -> str:
        return ((self.amount_of_curly_braces-1) * '{') + string + ((self.amount_of_curly_braces-1) * '}')

    def __repr__(self) -> str:
        return '\'' + self.f_string_parse() + '\''

    def __str__(self) -> str:
        return self.f_string_parse()


def main() -> None:
    global hello, world
    hello = "Hello,"
    world = "wo" 
    world = ['5','4','5']
    string = f("{{{hello!a}}} {world[1]}hiyyy")
    string1 = f'{{{hello!a}}} {world[1]}hiyyy'
    tests = []
    tests.append('len of fake f_string ' + str(len(string)))
    # need to work on calling f_string.f from another variable
    tests.append('fake f_string ' + f(string))
    tests.append('len of real f_string ' + str(len(string1)))
    tests.append('real f_string ' + string1)
    boxify(tests)
    # z= f.curly_bracealize()
    # print(z)
    # need to fix type


if __name__ == '__main__':
    main()
