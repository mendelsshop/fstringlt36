#!/usr/bin/env python3
import re
import logging
import inspect
import regexs
import sys

pythonv = sys.version.split('(')[0]
# print('python version:', pythonv)
# should probably do a better job for logging
# next feaure detect amount of curly braces and based that reurn either an evaluted or unevaluated vairable encapsulted in a certain amount of curly braces

class f(str,object):

    def __new__(cls, *args, **kwargs):
        return super(f, cls).__new__(cls, *args, **kwargs)

    def __init__(self, string) -> None:
        self.logger = logging
        if sys.version_info > (3, 9):
            self.logger.basicConfig(
                filename='debug.log',
                encoding='utf-8',
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
                level=logging.DEBUG)
            # print('3.9 or above')

        else:
            self.logger.basicConfig(
                filename='debug.log',
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
                level=logging.DEBUG)
            # print('3.8 or lower')
        

        self.pythonv = pythonv
        self.logger.debug('python version: %s', self.pythonv)
        self.string = string
        # should probably move this to a config file or take it from setup.py
        self.version = '0.0.2-alpha'
        self.regex0 = regexs.regex0
        self.regex1 = regexs.regex1
        self.scope = inspect.stack()[1][0]
        self.logger.info('Started')
        self.output = self.f_string_parse()
        string = self.output
        # print(string)
        # print(self.output)
        # print(self.string)
        self.logger.info('Finished')

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
        # need to check if its the last no space char or if its followed by !s, !a or !r
        # so that it does not split in middle the variable/string
        # if the last match from self.regex10('=').findall(string):
        #     equal = self.regex10('=').findall(string)[-1]

        if self.regex1('=').findall(string):
            # check if the = is part of an operator
            equal = True
            string = self.regex1('=').split(string)
            
        if type(string) is str:
            string = [string, '']

        return string, equal

    def type_conversions(self, string) -> str:
        strcpy = string
        if '!' in string:
            string = string.split('!')
            # if string conatain anything besides for a, s, or r
            if string[1] not in ['a', 's', 'r']:
                # if string does not start with a, s, or r
                if string[1][0] not in ['a', 's', 'r']:
                    raise SyntaxError("SyntaxError: f-string: invalid conversion character: expected 's', 'r', or 'a'")
                
                else:
                    # if after with a, s, or r there is anything else
                    if string[1][1:]:
                        raise SyntaxError("f-string: expecting '}'")

            elif string == '=':
                return None, strcpy 

            else:
                return '!' + string[1], string[0]

        return None, strcpy

    def var_to_string(self, string, ogstring, format=None, equal=None, type_conversion=None) -> str:
        '''
        this function takes a string
        trys to evaluate the string first in the local scope
        and then in the global scope
        if still nothing is found catches the NameError 
        and optinally if the string has a format
        returns a string of the variable
        '''

        if type(format) is str:
            # check if python version is 2.6 or greater
            # if this is true we can use str.format() because 2.6 is the oldest version to support it
            if self.pythonv >= '2.6':
                pass
            try:
                self.logger.info('finding the value of whats in string based on locals')
                # need to figure out how to evaluate format codes
                value = eval(format % eval(string, None, self.get_scope(string)))

            except NameError:
                self.logger.error('variable ' + string + ' not found')
                self.logger.info('finding the value of whats in string based on globals')
                value = eval(format % eval(string, None, self.get_global_scope(string)))

        else:
            try:
                self.logger.info('finding the value of whats in string based on locals')
                value = eval(string, None, self.get_scope(string))

            except NameError:
                self.logger.error('variable ' + string + ' not found')
                self.logger.info('finding the value of whats in string based on globals')
                value = eval(string, None, self.get_global_scope(string))
        
        if type_conversion:
            if type_conversion == '!a':
                # need to fix error with unicode characters and regex
                # print('ascci', ascii(value))
                value = ascii(value)

            elif type_conversion == '!s':
                value = str(value)

            elif type_conversion == '!r':
                value = repr(value)

            value1 =self.regex1('!').split(ogstring)[0]

        if equal:
            if type_conversion: return value1 + value

            return ogstring + self.__repr__(value)

        return value

    def f_string_parse(self) -> str:
        # print('iteerating through string')
        self.logger.info('parsing starts')
        for match in self.regex0.findall(self.string):
            # this can split in middle string so we need to figure out after sometthing else not if : in to in qoutes
            # we need to also check if : is followed by an operator like :=
            split_match = self.regex1(':').split(match[1:-1])
            try:
                format = split_match[1]
            except IndexError:
                format = None

            # print(format, 'format code')
            self.scope = inspect.stack()[1][0]
            # print(split_match[0],'split match')
            equals = self.str_equal_string(split_match[0])
            string = self.str_equal_string(split_match[0])[0][0]
            equal = self.str_equal_string(split_match[0])[1]
            # print(equal, 'after = ')
            # print(string, 'string')

            if equal:
                type_conversion = self.type_conversions(equals[0][-1])[0]
                
            else:
                type_conversion = self.type_conversions(split_match[0])[0]
                string = self.type_conversions(split_match[0])[1]

            # print(type_conversion, 'type conversion')
            # print(string, 'string')
            s = self.var_to_string(string, split_match[0], equal=equal, type_conversion=type_conversion, format=format)
            self.string = self.string.replace(match, s)
            # using re.sub messes with unicode and errors out wit bad escape \U so until i figure it out i will use str.replace()
            # self.output = re.sub(match, s, self.output)
        # amount of curly braces shoould be handled here
        self.logger.info('parsing end')
        return self.string

    def curly_bracealize(self, string, amount=1) -> str:
        '''
        returns string encapsulated in an amount of {} based on arg amount
        amount defaults to 1
        '''
        return (amount * '{') + str(string) + (amount * '}')
    # check
    def __len__(self) -> int:
        return len(self.output)
    # check
    def __repr__(self, string=None) -> str:
        if string:
            return repr(string)
        return repr(self.output)
    # check
    def __str__(self, string=None) -> str:
        # print(self)
        if string:
            return str(string)
        return str(self.output)
    # check
    # def __call__(self):
        # raise TypeError('\'str\' is not callable')
    # check
    def __radd__(self, string):
        return string + self.output
    # check
    def __add__(self, string):
        return self.output + string
    # check
    def __iadd__(self, string):
        self.output += string
        return self
    # maybe idk
    def __iter__(self):
        return iter(self.output)
    # check
    def __getitem__(self, index):
        print(self.string[index])
        return self.string[index]
    # check  
    # def __setitem__(self, index, value):
        # raise TypeError('\'str\' object does not support item assignment')
    # check  
    # def __delitem__(self, index):
    #     del self.output[index]
    #     return self.output
    # check 
    def __contains__(self, item):
        return item in self.output

    # def __getattr__(self, name):
        # return getattr(self.output, name)

    # def __setattr__(self, name, value):
        # setattr(self.output, name, value)
        # return self
    
    # def __delattr__(self, name):
    #     delattr(self.output, name)
    #     return self

    # def __lt__(self, other):
    #     return self.output < other

    # def __le__(self, other):
    #     return self.output <= other

    # def __eq__(self, other):
    #     return self.output == other

    # def __ne__(self, other):
    #     return self.output != other

    # def __gt__(self, other):
    #     return self.output > other

    # def __ge__(self, other):
    #     return self.output >= other

    # def __hash__(self):
    #     return hash(self.output)

    # def __nonzero__(self):
    #     return bool(self.output)

    # def __getstate__(self):
    #     return self.output

    # def __setstate__(self, state):
    #     self.output = state

    # def __reduce__(self):
    #     return self.output

    # def __class__(self):
        # return '<class \'str\'>'
    def upper(self):

        return self.output.upper()

    def lower(self):
        return self.output.lower()
    
    def capitalize(self):
        return self.output.capitalize()

    def __unicode__(self):
        return self.output

    def casefold(self) -> str:
        return super().casefold()




def main():
    print('to test it use the tests.py in the test directory')
    print('or import into you\'re own file using from f_string_lt_36 import f')


if __name__ == '__main__':
    main()