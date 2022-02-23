#!/usr/bin/env python3
import re

regex0 = re.compile(r'\{+.+?\}+', re.MULTILINE | re.UNICODE)
regex1 = lambda x: re.compile(
    r'(?<!\'|\"|\()'
    + x
    + r'(?!\'|\"|\))(?# regex for a character defined from the lambda not in quotes or parentheses)',
    re.MULTILINE | re.UNICODE,
)
# it turns out that regex0 is not correct for fstring parsing beccause i did not understand fully what multiple '{' mean
# basic outline for the new regex is:
# match only single {} not double like this {{}} 
# any {{ = {, and }} = } basically {{ is an escape for { in and fstring and the same thing for }
# fstring = 'literal | '{{' | '}}' | {[expression][=]['!r' |' !a' | 's' ][:format_spec=fstring]}]}'
# format_spec can be none ie f'{x} or f'{x:.2f}' or f'{x:.{y}f} so in essence an fstring in an fstring and maybee you could run into a recursion error
# thinking about it, i will need to use a for loop and loop over the whoole string
# example of fstring parsing
# f'{3} {1} {{{5*5}'
# will be parsed as
# '3 1 {25'
# first we use a regex to replace all '{{' that are not in any form of quotes or parenthsis with something not '{', f'{{{5*5:{4}}'}}}' -> f'`{25:{4}}}}' in this case where using '`' to replce '{{'
# then we have to find fstring expressions and evaluate/replcae them  and not any extra '}' f'`{25:{4}}}} -> f'`  025}}' so want to get {5*5:{4}} and not {5*5:{4}}}} so thats why were not also replacing '}}' with something else yet
# so when we find '{' with a regex we need to check if it is in quotes or parentheses if its not wefind the next '}' and if theres another '{' we need to find the next '}' and so on this probably could be done with a for loop
# then we have to replace all '}}' with something not '}' f'`  025}}' -> f'`  025?' in this example where using '?' to replace '}}'
# now we check for any '{' or '}' if they are any left raise an error
# finally we replace all '`' with '{' and '?' with '}' f'`  025?' -> f'{025}'
# some of this is tooken from the python docs https://docs.python.org/3.11/reference/lexical_analysis.html#formatted-string-literals and https://docs.python.org/3.11/library/string.html#format-specification-mini-language


