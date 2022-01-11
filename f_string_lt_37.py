#!/usr/bin/env python3
import re
import logging
import inspect

# should probably do a better job for logging
logger = logging
logger.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)

# use regex \{.+\} to match {hello}


# it looks like I will need to use the inspect library for turning strings into variables instead of the current var_handle
class f(str):

    def __init__(self, string =None) -> None:
        # dummy_var is just for catching whatever doesnt work so far like padding
        self.string = string
        self.output = ''
        self.version = '0.0.1-alpha'
        self.regex = re.compile(r'\{+.+?\}+',re.MULTILINE | re.UNICODE)
        self.last_index = 0
        logger.info('Started')

    def get_scope(self, string) -> dict:
        '''
        this function returns a dict of global variables if the string provided is in the global scope
        or else it returns a dict of None
        '''
        # print(string)
        scope = inspect.stack()[1][0]
        while string not in scope.f_locals:
            scope = scope.f_back
            if scope is None:
                return dict()
            return scope.f_locals

    def get_global_scope(self, string) -> dict:
        '''
        this function returns a dict of global variables if the string provided is in the global scope
        or else it returns a dict of None
        '''
        # print(string)
        scope = inspect.stack()[1][0]
        while string not in scope.f_globals:
            scope = scope.f_back
            if scope is None:
                return dict()
            return scope.f_globals

    def var_to_string(self, string) -> str:
        '''
        this function takes a string and returns a string of the variable
        it favors local variables over global variables
        so it will only return a global variable if it is not defined in the local scope
        '''
        # i got this from https://github.com/rinslow/fstring/blob/master/fstring/fstring.py
        try:
            value = eval(string, None, self.get_scope(string))

        except NameError:
            try:
                value = eval(string, None, self.get_global_scope(string))
                

            except NameError: 
                value = 'error: variable ' + string + ' not found'
        return value

    def f_string_parse(self) -> str:
        logger.info('parsing starts')
        # potato is just a dummy value until I can evaluate the string
        subst = "potato"
        self.output = self.regex.sub(subst, self.string, 0)
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

def main():
    pass

if __name__ == '__main__':
    main()