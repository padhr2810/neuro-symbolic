"""
TRICK
ORD() = IMPLIES ORDINAL().
	CONVERTS A UNICODE CHARACTER TO AN ORDINAL NUMBER. I.E. UNIQUE NUM THAT IDENTIFIES EACH CHAR IN THE VAST CATALOG OF TEXT SYMBOLS USED BY COMPUTERS.
CHR() = OPPOSITE OF ORD(). I.E. INT TO UNICODE CHARACTER.
ALSO NEED TO CONSIDER EDGE CASE WHERE '-' AT THE START.
"""

import functools
import string

#from test_framework import generic_test
#from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:

    print(f"\n\n\n\n\n#################################################################################")
    print(f"New input = {x}")

    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        
        print(f"\n################################ x % 10 = {x % 10}")
        print(f"ord('0') = {ord('0')}")
        print(f"ord('0') + x % 10 = {ord('0') + x % 10}")
        print(f"chr(ord('0') + x % 10) = {chr(ord('0') + x % 10)}")
        print(f"x = {x}")
        
        x //= 10
        if x == 0:
            break
    # Adds the negative sign back if is_negative
    print(f"\n#####\nresult before reversal = {s}")
    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(s: str) -> int:
    print(f"\n\n\n\n\n#################################################################################")
    print("Args for reduce(func, seq) ..... applies a particular function (first arg) to all of the list elements in the sequence (2nd arg)")
    
    if s == "0":
        return 0
    if s[0] == "-":
        neg = True 
        s = s[1:]
    elif s[0] == "+": 
        neg = False
        s = s[1:]
    else:
        neg = False 

    print(f"Input = {s}")
    print(f"ord('0') = {ord('0')}")
    res = 0
    for ch in s:
        res *= 10
        print(f"char = {ch}; Unicode int for ch = {ord(ch)}")
        res += (ord(ch) - ord("0"))
    if neg: 
        res = -res 
    
    # BOOK APPROACH:
    #return (-1 if s[0] == '-' else 1) * functools.reduce(
    #    lambda running_sum, c: running_sum * 10 + string.digits.index(c),
    #    s[s[0] in '-+':], 0)
    
    return res 


#def wrapper(x, s):
#    if int(int_to_string(x)) != x:
#        raise TestFailure('Int to string conversion failed')
#    if string_to_int(s) != x:
#        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    res_1   = int_to_string(1)
    res_123 = int_to_string(123)
    res_1579 = int_to_string(1579)
    int_5   = string_to_int("5")
    int_135 = string_to_int("135")
    int_579 = string_to_int("579")
    
    print("\n\n############################# INT TO STRING:")
    print(f"1 = {res_1}")
    print(f"123 = {res_123}")
    print(f"1579 = {res_1579}")
    print("\n\n############################# STRING TO INT:")
    print(f"int_5 = {int_5}")
    print(f"int_135 = {int_135}")
    print(f"int_579 = {int_579}")
    
#    exit(
#        generic_test.generic_test_main('string_integer_interconversion.py',
#                                       'string_integer_interconversion.tsv',
#                                       wrapper))

