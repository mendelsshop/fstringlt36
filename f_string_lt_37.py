#!/usr/bin/env python3
import logging
logger = logging
# should probably do a better job for logging
logger.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
# fix spagghetti code in f class 
class f(str):

    def __init__(self, string) -> None:
        # dummy_var is just for catching whatever doesnt work so far like padding
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
        self.unhandled_var = ''
        self.dict_handling = False
        logger.info('Started')

    def phase_change(self, phase) -> None:
        '''
        this method if for changing the phase of the f class parsing
        the reason that it's in a method is because its easier to log/print in one place
        '''
        self.current_phase = phase
        logger.info('changing to ' + phase)
        return None

    def info(self) -> None:
        '''
        this metod is for logging/printing info about the f class
        while parsing the f string
        '''
        try:
            self.string[self.i]

        except IndexError:
            return False
        
        logger.info('version: ' + self.version)
        if self.current_phase:
            logger.info('current phase: ' + self.current_phase)

        if self.string[self.i]:
            logger.info('current substring: ' + self.string[self.i])
            
        if self.var:
            logger.info('var: ' + self.var)
            
        if self.output:
            logger.info('output: ' + self.output)

        if self.dummy_var:
            logger.info('dummy_var: ' + self.dummy_var)
            
        logger.info('var handling: ' + str(self.var_handling))
        
        logger.info('dict handling: ' + str(self.dict_handling))

        return None        

    def var_handle(self) -> None:
        # need to work on gloabal and local variables handling
        try:
            try:
                exec('global var')

            except:
                logger.info('global var not defined')

            self.var = eval(self.var)

        except NameError:
            logger.error('error: variable ' + self.var + ' not found')
            self.var = '(error: variable ' + self.var + ' not found)'

        except SyntaxError:
            logger.error('error: variable SyntaxError')
            self.var = 'error: variable SyntaxError'

    def f_string_parse(self) -> str:
        while len(self.string) > self.i:
            logger.info('================================================================')
            # for self.i in range(len(self.string)):       
            if self.current_phase == 'parsing':
                if self.string[self.i] == '{':
                    self.phase_change('f_string')
                    self.i += 1
                    self.info()
                    logger.info('changing to f_string parsing')
                      
                else:
                    self.output += self.string[self.i]
                    self.i += 1
                    self.info()
                    logger.info('adding to output')
                   
            elif self.current_phase == 'f_string':
                if self.string[self.i] in  ['\"','\''] and self.var_handling is True and self.string[self.i-1] != '[' and self.dict_handling is False:
                    self.var_handling = False
                    self.var += self.string[self.i]
                    self.i += 1
                    self.info()
                    print(self.var)
                    logger.info('adding to var without var handling')
                   
                elif self.string[self.i] in ['\'','\"'] and self.var_handling is False:
                    self.var_handling = True
                    self.i += 1
                    self.info()
                    logger.info('stop adding to var with var handling')

                elif self.string[self.i] == '{':
                    self.amount_of_curly_braces += 1
                    self.i += 1
                   
                elif self.string[self.i] == '}' and self.var_handling is True:
                    self.phase_change('parsing')
                    if self.var[0] in ['\'','\"']:
                        self.var = self.var.strip('\"\'')
                        self.unhandled_var = self.var
                
                    else:
                        self.unhandled_var = self.var
                        self.var_handle()

                    self.i += 1
                    if self.change_to in ['r','a']:
                        if self.change_to == 'r':
                            self.var = repr(self.var)

                        elif self.change_to == 'a':
                            # return ascci of var
                            self.var = ascii(self.var)
                            
                    if self.amount_of_curly_braces > 0:
                        if self.amount_of_curly_braces % 2 == 0:
                            self.amount_of_curly_braces -= 1
                            self.var = self.curly_bracealize(self.var)
                            self.i += (self.amount_of_curly_braces + 1)
                        
                        else:
                            self.var = self.curly_bracealize(self.unhandled_var)
                            self.i += self.amount_of_curly_braces 

                    self.change_to = ''
                    self.output += str(self.var)
                    self.var = ''
                    self.dummy_var = ''
                    self.is_in_lt_or_gt = False
                    self.should_be_padding = False
                    self.current_phase = 'parsing'
                    self.var_handling = True
                    self.amount_of_curly_braces = 0
                    self.dict_handling = False
                    logger.info('adding var to output')
                   
                elif (self.string[self.i] == ':' or self.string[self.i] == '!') and self.var_handling is True:
                    # probably shouldn't need to go after f_string parsing if ! and just do it here
                    self.phase_change('after f_string')
                    self.i += 1
                    self.info()
                    logger.info('changing to after f_string parsing')
                   
                else:
                    if self.string[self.i] in ['\'','\"'] and self.string[self.i-1] == '[':
                        self.dict_handling = True
                        logger.info('dict handling')
                    self.var += self.string[self.i]
                    logger.info('adding to var '+self.string[self.i] +' with var handling')
                    self.i += 1  
                    self.info()
                   
            elif self.current_phase == 'after f_string':
                if self.string[self.i] == '}':
                    self.phase_change('f_string')
                    self.info()
                    self.var_handling = True
                    logger.info('changing to f_string parsing')
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
                    logger.info('handling padding')

        logger.info('Done')
        return self.output

    def curly_bracealize(self,string) -> str:
        '''
        returns string encapsulated in {}
        '''
        return (self.amount_of_curly_braces * '{') + str(string) + (self.amount_of_curly_braces * '}')

    def __len__(self) -> int:
        return len(self.f_string_parse())

    def __repr__(self) -> str:
        return '\'' + self.f_string_parse() + '\''

    def __str__(self) -> str:
        return self.f_string_parse()