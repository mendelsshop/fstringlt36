import os
import sys
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
split_path.append('fstringlt36')
path = sep.join(split_path)
sys.path.append(path)
from fstringlt36 import f


class TestFString(TestCase):
    def test_hello(self):
        w = "World"
        testcase = str(f('Hello, {w}'))
        self.assertEqual(testcase, 'Hello, World')

    def test_type_flag(self):
        w = "World"
        testcase = str(f('Hello, {w !r}'))
        self.assertEqual(testcase, "Hello, 'World'")

    def test_lambda(self):
        w = "World"
        testcase = lambda x: str(f('Hello, {x}'))
        self.assertEqual(testcase(w), 'Hello, World')

        w = "World"
        testcase = str(f('Hello, {w}'))
        w = 'Different Value'
        self.assertEqual(testcase, 'Hello, World')

    def test_dot_capitalize(self):
        w = "bar"
        testcase = str(f('foo {w}').capitalize())
        self.assertEqual(testcase, 'Foo bar')

    def test_dot_upper(self):
        w = "bar"
        testcase = str(f('foo {w}').upper())
        self.assertEqual(testcase, 'FOO BAR')

    def test_dot_lower(self):
        w = "BAR"
        testcase = str(f('FOO {w}').lower())
        self.assertEqual(testcase, 'foo bar')

    def test_dot_title(self):
        w = "bar"
        testcase = str(f('foo {w}').title())
        self.assertEqual(testcase, 'Foo Bar')

    def test_dot_swapcase(self):
        w = "bar"
        testcase = str(f('FOO {w}').swapcase())
        self.assertEqual(testcase, 'foo BAR')

    def test_add(self):
        testcase = str(f('{1 + 1 = }'))
        self.assertEqual(testcase, '1 + 1 = 2')
