# i know i should be using unit test 
# but i don't know unit tests so this will do
from  f_string_lt_37 import f
def boxify(list) -> None:
    '''
    the boxify function is just way to test results in a nice boxify function
    first we find the larggest string in the list given to the boxify function
    then we print a hash/number sign times longest string + 4
    then we go through each iem in the list and print a hash/number sign than using the str.center() method we center the current string by the largest string
    followed by another hash/number sign
    than we again do the hash/number sign times longest string + 4
    '''
    # find larggest string in list
    larggest_string = len(max(list, key=len))
    print('#' *(larggest_string+4))
    for item in list:
        # center each item with .center(larggest_string)
        print('#',item.center(larggest_string), '#')
    print('#' *(larggest_string+4))
    

def main() -> None:
    '''
    just for visual testing
    returns None
    '''
    global hello, world
    hello = "Hello,"
    worlds = "wo" 
    world = {'stuff':'to'}
    world['thing'] = 'world'
    world['list'] = [1,'hi',3,4,5]
    world['tuple'] = (1,2,3,4,5)
    world['set'] = {1,2,3,4,5}
    world['function'] = lambda x: x**2
    string = f("{{hello}} {{{world['list'][0]}}}hiyyy")
    string1 = f'{{hello}} {{{world["list"][0]}}}hiyyy'
    tests = []
    tests.append('len of fake f_string ' + str(len(string)))
    tests.append('fake f_string ' + f(string))
    tests.append('len of real f_string ' + str(len(string1)))
    tests.append('real f_string ' + string1)
    boxify(tests)


if __name__ == '__main__':
    main()