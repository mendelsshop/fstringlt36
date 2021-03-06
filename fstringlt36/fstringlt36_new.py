import logging
import inspect
import re

# if imported from pip
try:
    from . import regexs
# if imported from tests/test.py
# or from tests/test_visual.py
# for python 3
except ImportError:
    import regexs
# for python 2
except ValueError:
    import regexs
import sys

pythonv = sys.version.split('(')[0]

# if python is 2.7 or lower
if pythonv < '3.0':
    from UserString import UserString
else:
    from collections import UserString
# should probably do a better job for logging
# next feaure detect amount of curly braces
# based that reurn either an evaluted or unevaluated vairable
# encapsulted in a certain amount of curly braces
# make sure that when something like f("{5 + 5")
# is evaluated it converts the eval of 5 * 5 to a string


class f(UserString):
    def __init__(self, string):
        self.logger = logging
        if sys.version_info > (3, 9):
            self.logger.basicConfig(
                filename='debug.log',
                encoding='utf-8',
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
                level=logging.DEBUG,
            )
            # print('3.9 or above')

        else:
            self.logger.basicConfig(
                filename='debug.log',
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
                level=logging.DEBUG,
            )
            # print('3.8 or lower')

        self.pythonv = pythonv
        self.logger.debug('python version: %s', self.pythonv)
        self.string = string
        # should probably move this to a config file or take it from setup.py
        self.version = '0.0.3-alpha'
        self.regex0 = regexs.regex0
        self.regex1 = regexs.regex1
        self.scope = inspect.stack()[1][0]
        self.logger.info('Started')
        try:
            print('data', self.data)
        except:
            pass
        self.data = self.f_string_parse(string)
        print('data', self.data)
        self.logger.info('Finished')

    # get_scope() and get_global_scope() can technicaly be combined
    def split_on_qoutes(self, item):
        for quotes in ['"', "'", '"""', "'''"]:
            try:
                item = item.split(quotes)
            except AttributeError:
                for quote in item:
                    quote = quote.split(quotes)
        return item

    def get_scope(self, string):
        '''
        this function returns a dict of global variables
        if the string provided is in the local scope
        or else it returns a dict of None
        this is from:
        https://github.com/rinslow/fstring/blob/master/fstring/fstring.py
        '''
        while string not in self.scope.f_locals:
            self.scope = self.scope.f_back
            if self.scope is None:
                return dict()

            return self.scope.f_locals

    def get_global_scope(self, string):
        '''
        this function returns a dict of global variables
        if the string provided is in the global scope
        or else it returns a dict of None
        this is from:
        https://github.com/rinslow/fstring/blob/master/fstring/fstring.py
        '''
        while string not in self.scope.f_globals:
            self.scope = self.scope.f_back
            if self.scope is None:
                return dict()

            return self.scope.f_globals

    def str_equal_string(self, string):
        equal = None
        # check if its the last no space char or its followed by !s, !a or !r
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

    def type_conversions(self, string):
        strcpy = string
        if '!' in string:
            string = string.split('!')
            # if string conatain anything besides for a, s, or r
            if string[1] not in ['a', 's', 'r']:
                # if string does not start with a, s, or r
                if string[1][0] not in ['a', 's', 'r']:
                    raise SyntaxError(
                        "SyntaxError: f-string: invalid conversion character: expected 's', 'r', or 'a'"
                    )

                else:
                    # if after with a, s, or r there is anything else
                    if string[1][1:]:
                        raise SyntaxError("f-string: expecting '}'")

            elif string == '=':
                return None, strcpy

            else:
                return '!' + string[1], string[0]

        return None, strcpy

    def var_to_string(
        self, string, ogstring, format=None, equal=None, type_conversion=None
    ):
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
            # if this is true we can use str.format()
            # because 2.6 is the oldest version to support it
            if self.pythonv >= '2.6':
                pass
            try:
                self.logger.info(
                    'finding the value of whats in string based on locals'
                )
                # need to figure out how to evaluate format codes
                value = eval(
                    format % eval(string, None, self.get_scope(string))
                )

            except NameError:
                self.logger.error('variable ' + string + ' not found')
                self.logger.info(
                    'finding the value of whats in string based on globals'
                )
                value = eval(
                    format % eval(string, None, self.get_global_scope(string))
                )

        else:
            try:
                self.logger.info(
                    'finding the value of whats in string based on locals'
                )
                value = eval(string, None, self.get_scope(string))

            except NameError:
                self.logger.error('variable ' + string + ' not found')
                self.logger.info(
                    'finding the value of whats in string based on globals'
                )
                value = eval(string, None, self.get_global_scope(string))

        if type_conversion:
            if type_conversion == '!a':
                # need to fix error with unicode characters and regex
                value = ascii(value)

            elif type_conversion == '!s':
                value = str(value)

            elif type_conversion == '!r':
                value = repr(value)

            value1 = self.regex1('!').split(ogstring)[0]

        if equal:
            if type_conversion:
                return value1 + value

            return ogstring + repr(value)

        return value

    def f_string_parse(self, string):
        replace = []
        # string = re.sub(r'{{', '_', string)
        # string = re.sub(r'}}', '_', string)
        # split string on quotes ie ', ", ''', """
        quotesstring = self.split_on_qoutes(string)

        print(quotesstring)

        replacestring = []
        
        for index, char in enumerate(string):
            print(char, index)
            if char == '{':
                if replace:
                    if replace[-1][0] == char and replace[-1][1] == (index -1):
                        replace.pop()
                replace.append((char, index))
            elif char == '}':
                replace.append((char, index))
        print(replace)

        if len(replace) % 2 != 0:
            raise SyntaxError("SyntaxError: f-string: unbalanced braces")
        for i in replace:
            if i[1] % 2 == 0:
                continue
            print(i)
            # find the n ext item in replace
            
            s = string[(i[1]+1)]
                
                

        print('replace', replace)
        return string


        
        

    def curly_bracealize(self, string, amount=1):
        '''
        returns string encapsulated in an amount of {} based on arg amount
        amount defaults to 1
        '''
        return (amount * '{') + str(string) + (amount * '}')


def main():
    print('to test it use the tests.py in the test directory')
    print('or import into you\'re own file using from fstringlt36 import f')


if __name__ == '__main__':
    main()
