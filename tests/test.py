#!/usr/bin/env python3
import os
import sys
import unittest
from unittest import TestCase, main, skipIf, expectedFailure

# i know i should be using unit test
# but i don't know unit tests so this will do
if os.name == 'nt':
    sep = '\\'
else:
    sep = '/'
    
# gets the path to src directories
path = os.path.dirname(os.path.realpath(__file__))
split_path = path.split(sep)
split_path.pop(-1)
split_path.append('src')
path = sep.join(split_path)
sys.path.append(path)
from f_string_lt_36 import f

class TestFString(TestCase):
    def test_hello(self):
        w = "World"
        testcase = str(f('Hello, {w}'))
        self.assertEqual(testcase, 'Hello, World')

    def test_type_flag(self):
        w = "World"
        testcase = str(f('Hello, {w !r}'))
        self.assertEqual(testcase, "Hello, 'World'")