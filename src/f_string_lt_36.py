#!/usr/bin/env python3
import re
import logging
import inspect
import regexs
# should probably do a better job for logging
# next feaure detect amount of curly braces and based that reurn either an evaluted or unevaluated vairable encapsulted in a certain amount of curly braces

class f(str):

    def __init__(self, string) -> None:
        self.logger = logging
        self.logger.basicConfig(
            filename='debug.log',
            encoding='utf-8',
            level=logging.DEBUG)
        self.string = string
        self.output = string
        # should probably move this to a config file or take it from setup.py
        self.version = '0.0.2-alpha'
        self.regex0 = regexs.regex0
        self.regex1 = regexs.regex1
        self.scope = inspect.stack()[1][0]
        self.logger.info('Started')

    # get_scope() and get_global_scope() can technicaly be combined
    def get_scope(self, string) -> dict:
        '''
        this function returns a dict of global variables
        if the string provided is in the local scope
        or else it returns a dict of None
        this is from https://github.com/rinslow/fstring/blob/master/fstring/fstring.py
        '''
        while string not in self.scope.f_locals:
            self.scope = self.scope.f_back
            if self.scope is None:
                return dict()

            return self.scope.f_locals

    def get_global_scope(self, string) -> dict:
        '''
        this function returns a dict of global variables
        if the string provided is in the global scope
        or else it returns a dict of None
        this is from https://github.com/rinslow/fstring/blob/master/fstring/fstring.py
        '''
        while string not in self.scope.f_globals:
            self.scope = self.scope.f_back
            if self.scope is None:
                return dict()

            return self.scope.f_globals

    def str_equal_string(self, string) -> tuple:
        equal = None
        if self.regex1('=').search(string):
            equal = True
            string = self.regex1('=').split(string)[0]
        return string, equal

    def type_conversions(self, string) -> str:
        if self.regex1('!').search(string):
        
            # if theres a space at the end of the string
            # raise an error
            string = repr(self.regex1('!').split(string)[1])
            print(string[-1])
            if string[-1].isspace():
                raise SyntaxError(" f-string: expecting '}'")


    def var_to_string(self, string, ogstring, format=None, equal=None) -> str:
        '''
        this function takes a string
        trys to evaluate the string first in the local scope
        and then in the global scope
        if still nothing is found catches the NameError 
        and optinally if the string has a format
        returns a string of the variable
        '''

        if type(format) is str:
            try:
                self.logger.info('finding the value of whats in string based on locals')
                value = eval('format' % eval(string, None, self.get_scope(string)))

            except NameError:
                value = 'error: variable ' + string + ' not found'
                self.logger.error('variable ' + string + ' not found')
    
                try:
                    self.logger.info('finding the value of whats in string based on globals')
                    value = eval('format' % eval(string, None, self.get_global_scope(string)))

                except NameError:
                    value = 'error: variable ' + string + ' not found'
                    self.logger.error('variable ' + string + ' not found')

        else:
            try:
                self.logger.info('finding the value of whats in string based on locals')
                value = eval(string, None, self.get_scope(string))

            except NameError:
                value = 'error: variable ' + string + ' not found'
                self.logger.error('variable ' + string + ' not found')
                try:
                    self.logger.info('finding the value of whats in string based on globals')
                    value = eval(string, None, self.get_global_scope(string))

                except NameError:
                    value = 'error: variable ' + string + ' not found'
                    self.logger.error('variable ' + string + ' not found')
        
        if equal:
            return ogstring + self.__repr__(value)

        return value

    def f_string_parse(self) -> str:
        self.logger.info('parsing starts')
        for match in self.regex0.findall(self.string):
            split_match = self.regex1(':').split(match[1:-1])
            self.scope = inspect.stack()[1][0]
            string = self.str_equal_string(split_match[0])[0]
            equal = self.str_equal_string(split_match[0])[1]
            type_conversion = self.type_conversions(split_match[0])
            self.output = re.sub(match, self.var_to_string(string, split_match[0], equal=equal), self.output)
        # amount of curly braces shoould be handled here
        self.logger.info('parsing end')
        return self.output

    def curly_bracealize(self, string, amount=1) -> str:
        '''
        returns string encapsulated in an amount of {} based on arg amount
        amount defaults to 1
        '''
        return (amount * '{') + str(string) + (amount * '}')

    def __len__(self) -> int:
        return len(self.f_string_parse())

    def __repr__(self, string=None) -> str:
        if string: return '\'' + string + '\''
        return '\"' + self.f_string_parse() + '\"'

    def __str__(self) -> str:
        return self.f_string_parse()


def main():
    pass


if __name__ == '__main__':
    main()
