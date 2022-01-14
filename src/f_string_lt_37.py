#!/usr/bin/env python3
import re
import logging
import inspect
# should probably do a better job for logging


class f(str):

    def __init__(self, string) -> None:
        self.logger = logging
        self.logger.basicConfig(
            filename='debug.log',
            encoding='utf-8',
            level=logging.DEBUG)
        self.string = string
        self.output = string
        self.version = '0.0.1-alpha'
        self.scope = inspect.stack()[1][0]
        self.regex = re.compile(r'\{+.+?\}+', re.MULTILINE | re.UNICODE)
        self.logger.info('Started')

    # get_scope() and get_global_scope() can technicaly be combined
    def get_scope(self, string) -> dict:
        '''
        this function returns a dict of global variables
        if the string provided is in the local scope
        or else it returns a dict of None
        '''
        scope = self.scope
        print(scope)
        while string not in scope.f_locals:
            scope = scope.f_back
            if scope is None:
                return dict()

            return scope.f_locals

    def get_global_scope(self, string) -> dict:
        '''
        this function returns a dict of global variables
        if the string provided is in the global scope
        or else it returns a dict of None
        '''
        scope = self.scope
        while string not in scope.f_globals:
            scope = scope.f_back
            if scope is None:
                return dict()

            return scope.f_globals

    def var_to_string(self, string, _global=None, format=None) -> str:
        '''
        this function takes a string
        optinally if the string is in the global scope
        and optinally if the string has a format
        returns a string of the variable
        '''
        # could probably be cut down a bit
        # this is from https://github.com/rinslow/fstring/blob/master/fstring/fstring.py
        if type(format) is str:
            if _global is None:
                try:
                    self.logger.info('finding the value of whats in string based on locals')
                    value = eval('format' % eval(string, None, self.get_scope(string)))

                except NameError:
                    value = 'error: variable ' + string + ' not found'
                    self.logger.error('variable ' + string + ' not found')
            else:
                try:
                    self.logger.info('finding the value of whats in string based on globals')
                    value = eval('format' % eval(string, None, self.get_global_scope(string)))

                except NameError:
                    value = 'error: variable ' + string + ' not found'
                    self.logger.error('variable ' + string + ' not found')

        else:
            if _global is None:
                try:
                    self.logger.info('finding the value of whats in string based on locals')
                    value = eval(string, None, self.get_scope(string))

                except NameError:
                    value = 'error: variable ' + string + ' not found'
                    self.logger.error('variable ' + string + ' not found')

            else:
                try:
                    self.logger.info('finding the value of whats in string based on globals')
                    value = eval(string, None, self.get_global_scope(string))

                except NameError:
                    value = 'error: variable ' + string + ' not found'
                    self.logger.error('variable ' + string + ' not found')

        return value

    def f_string_parse(self) -> str:
        self.logger.info('parsing starts')
        for match in self.regex.findall(self.string):
            try:
                self.output = re.sub(match, self.var_to_string(match[1:-1]), self.output)

            except NameError:
                self.output = re.sub(match, self.var_to_string(match[1:-1], _global=True), self.output)

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

    def __repr__(self) -> str:
        return '\'' + self.f_string_parse() + '\''

    def __str__(self) -> str:
        return self.f_string_parse()


def main():
    pass


if __name__ == '__main__':
    main()
