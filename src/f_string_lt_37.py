#!/usr/bin/env python3
import re
import logging
import inspect

# should probably do a better job for logging


# use regex \{.+\} to match {hello}


# it looks like I will need to use the inspect library for turning strings into variables instead of the current var_handle
class f(str):

    def __init__(self, string =None) -> None:
        # dummy_var is just for catching whatever doesnt work so far like padding
        self.logger = logging
        self.logger.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
        self.string = string
        self.output = ''
        self.version = '0.0.1-alpha'
        # regex breakdown \{+ for 1 or more {, .+? for everything in the curly braces
        # need to fix space in when using more than 1
        self.regex = re.compile(r'\{+.+?\}+',re.MULTILINE | re.UNICODE)
        self.subst_val = "potato"
        self.logger.info('Started')

    # get_scope() and get_global_scope() can technicaly be combined
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
        # to make fomater specifiers work:
        # i will have to have a double eval()
        # like this: value = eval('format specifier' % eval(string, None ,self.get_scope(string)))
        print(string)
        try:
            self.logger.info('finding the value of whats in string based on locals')
            value = eval(string, None, self.get_scope(string))
            
        # this might catch other errors besides for string not being in locals 
        # but im just asssuming any error is a edge case so i dont care
        except NameError:
            try:
                self.logger.info('finding the value of whats in string based on globals')
                value = eval(string, None, self.get_global_scope(string))
                
            except NameError: 
                value = 'error: variable ' + string + ' not found'
                self.logger.info('variable ' + string +' not found')
        return value

    def f_string_parse(self) -> str:
        self.logger.info('parsing starts')
        # potato is just a dummy value until I can evaluate the string
        # have to loop over the regex findall() then replace the {} with the evaluated string
        for match in self.regex.findall(self.string):
            print(match[1:-1])
            self.output = re.sub(match, self.var_to_string(match[1:-1]), self.string)
        # might have to update var_to_string to accept fomat specifiers ie %s %d %f etc
        # amount of curly braces shoould be handled here

        # self.output = self.regex.sub(self.subst_val, self.string, 0)
        self.logger.info('parsing end')
        return self.output

    def curly_bracealize(self, string, amount = 1) -> str:
        '''
        returns string encapsulated in an amount of {} based on function arg amount
        amount defaults to 1
        '''
        return (amount * '{') + str(string) + (amount * '}')

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