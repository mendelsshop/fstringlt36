import os
import sys

if os.name == 'nt':
    sep = '\\'
else:
    sep = '/'
import sys

# gets the path to src directories
path = os.path.dirname(os.path.realpath(__file__))
split_path = path.split(sep)
split_path.pop(-1)
split_path.append('fstringlt36')
path = sep.join(split_path)
# kinda hacky way to import the fstring module from the src folder
# because when I tried to import fstring like this:
# from ..src.f_string_lt_37 import f
# or any variation of that it would not work
sys.path.append(path)
from fstringlt36 import f
# creates a test class



def boxify(list):
    '''
    the boxify function is just way to test results in a nice boxify function
    first we find the larggest string in the list given to the boxify function
    then we print a hash/number sign times longest string + 4
    then we go through each iem in the list and print a hash/number sign
    than using the str.center() method we center the current string by the largest string
    followed by another hash/number sign
    than we again do the hash/number sign times longest string + 4
    '''
    # find larggest string in list
    larggest_string = len(max(list, key=len))
    print('#' * (larggest_string+4))
    for item in list:
        # center each item with .center(larggest_string)
        print('# ' + item.center(larggest_string) + ' #')
    print('#' * (larggest_string + 4))


def main():
    '''
    just for visual testing
    returns None
    '''

    hello = "Hello,"
    worlds = "wo"
    emoji = "🤓"
    world = {'stuff': 'to'}
    world['thing'] = 'world'
    world['list'] = [1, 'hi', 3, 4, 5]
    world['tuple'] = (1, 2, '4', 5)
    val = 5 * 5
    world['set'] = {1, 2, 3, '4', 5}
    world['function'] = lambda x: x**2
    
    string = f('{emoji} {worlds}')
    tests = []
    tests.append('len of fake f_string ' + str(len(string)))
    tests.append('fake f_string ' + string)

    # if python supports f-strings
    if sys.version_info > (3, 6):
        string1 = eval("f'{emoji} {worlds}'")
        tests.append('len of real f_string ' + str(len(string1)))
        tests.append('real f_string ' + string1)
    else:
        tests.append('real f_string not supported')
    boxify(tests)


if __name__ == '__main__':
    main()
