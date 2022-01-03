#!/usr/bin/env python3
import logging
# should probably do a better job for logging
logger = logging
logger.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)

# use regex \{.+\} to match {hello}
# it looks like I will need to use the inspect library for turning strings into variables instead of the current var_handle
class f(str):

    def __init__(self, string) -> None:
        # dummy_var is just for catching whatever doesnt work so far like padding
        self.string = string
        self.output = ''
        self.version = '0.0.1-alpha'
        logger.info('Started')

    def var_handle(self) -> None:
        # need to work on gloabal and local variables handling
        try:
            try:
                exec('global var')

            except:
                logger.info('global var not defined')

            self.var = eval(self.var)

        except NameError:
            logger.error('error: variable name not found')
            self.var = 'error: variable name not found'

        except SyntaxError:
            logger.error('error: variable')
            self.var = 'error: variable'

    def f_string_parse(self) -> str:
        logger.info('parsing starts')
        logger.info('parsing end')
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


