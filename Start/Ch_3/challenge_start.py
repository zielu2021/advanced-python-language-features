# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

l = 0
num_char = 0
num_punct = 0
num_unique = 0
unique_str = ""

def calc_values(the_str):
    global l, num_char, num_punct, num_unique, unique_str

    l = len(the_str)

    # count the number charatcters
    num_char = len([c for c in the_str if c.isnumeric()])

    #count the punctuation characters
    num_punct = len([c for c in the_str if c in string.punctuation])

    unique_str = "".join({c for c in the_str if c.isalpha()})
    num_unique = len(unique_str)
    

    print(l)
    print(num_char)
    print(num_punct)
    print(unique_str)
    print(unique_str)

calc_values(test_str)
