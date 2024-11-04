"""
TRICK
2-STEP PROCESS. I: CONVERT STR-BASE1 TO INT TYPE BASE 10. II: THEN CONVERT INT TO STR-BASE2.
MY METHOD BELOW IS MUCH EASIER TO FOLLOW THAN THE METHOD USED IN THE BOOK.
	BECAUSE I AVOID "reduce" AND "lambda" AND I AVOID RECURSION.
USE string.hexdigits.index(s) TO CONVERT STRING NUMBER (SINGLE CHAR, E.G. '2') INTO AN INT TYPE
string.hexdigits is a pre-initialized string used as string constant. i.e. string = the hexadecimal letters ‘0123456789abcdefABCDEF’.
	Parameters : Doesn’t take any parameter, since it’s not a function. Merely a string that you can call.

"""

import functools
import string

#from test_framework import generic_test

# 3 INPUTS:
num_as_string = "255" 
b1 = 10 
b2 = 2 

def pr_convert_base(num_as_string: str, b1: int, b2: int) -> str:

    is_negative = num_as_string[0] == '-'
    if is_negative:
        num_as_string = num_as_string[1:]
    
    int_intermediate_abs = 0
    power=0
    for x in reversed(num_as_string):
        multiplier = 1*(b1**power)
        int_intermediate_abs += (string.hexdigits.index(x)*multiplier)
        power+=1
    print(f"int_intermediate_abs= {int_intermediate_abs}")

    output_str = ""
    while int_intermediate_abs:
        output_str += string.hexdigits[int_intermediate_abs % b2]
        int_intermediate_abs //= b2
    output_str = "".join(reversed(output_str))
    
    if is_negative:
        output_str = "-" + output_str

    print(f"output_str = {output_str}")
    return output_str
    
print("\n\n255, 10, 2")
print(pr_convert_base("255", 10, 2))

print("\n\n11111111, 2, 10")
print(pr_convert_base("11111111", 2, 10))

print("\n\n8, 10, 8")
print(pr_convert_base("8", 10, 8))

print("\n\n-8, 10, 8")
print(pr_convert_base("-8", 10, 8))

close() 

    
    

"""
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def construct_from_base(num_as_int, base):
        print(f"\n###### Run construct_from_base ######")
        print(f"num_as_int // base = {num_as_int // base}")
        print(f"num_as_int % base = {num_as_int % base}")
        print(f"string.hexdigits[num_as_int % base].upper() = {string.hexdigits[num_as_int % base].upper()}")
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    print(f"same str to int as previous 6_1, but use 'hexdigits' here to generalise it")
    
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))
"""


if __name__ == '__main__':
    res255 = convert_base("255", 10, 2)
    print(f"res255 = {res255}") 
    close() 
    
    res1000 = convert_base("1000", 10, 100)
    res100 = convert_base("100", 10, 100)

    print(f"res1000 = {res1000}") 
    print(f"res100 = {res100}") 
    
    print(string.hexdigits[2])
    print(string.hexdigits[4])
    print(string.hexdigits[11])
    #exit(
    #    generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
    #                                   convert_base))
