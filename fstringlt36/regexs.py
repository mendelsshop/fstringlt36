#!/usr/bin/env python3
import re

regex0 = re.compile(r'\{+.+?\}+', re.MULTILINE | re.UNICODE)


def regex1(x): return re.compile(
    r'(?<!\'|\"|\()' +
    x +
    r'(?!\'|\"|\))(?# regex for a character defined from the lambda not in quotes or parentheses)',
    re.MULTILINE | re.UNICODE)
