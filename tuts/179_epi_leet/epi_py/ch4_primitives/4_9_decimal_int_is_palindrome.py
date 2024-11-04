"""
TRICK #1:  LSD = X % 10
TRICK #2:  MSD = X // (10 ** (N-1)) 
TRICK #3:  NUM DIGITS = "math.floor(math.log10(x)) +1  "
TRICK #4:  ITERATE OVER "range(num_digits // 2)"
TRICK #5:  REMOVE THE MSD:
           "x %= msd_mask"
           I.E. WHERE "msd_mask" = "10** (num_digits -1)
TRICK #6: THE NUMBER LOSES 2 DIGITS EACH TIME, SO NEED TO ADJUST THE "msd_mask" EACH ITERATION OBVIOUSLY. SIMPLY DO THIS BY "msd_madk //= 100"
           
"""

import math


def is_palindrome_number(x: int) -> bool:

    """
    Round numbers down to the nearest integer:
    """
    
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    print(f"\n\n\n\n\n###################################################################################") 
    print(f"##############\n##############\nInput: {x}\n") 
    print(f"math.log10(x) = {math.log10(x)}")
    print(f"math.floor(math.log10(x)) = {math.floor(math.log10(x))}")
    print(f"num_digits = {num_digits}")
    
    msd_mask = 10**(num_digits - 1)
    print(f"msd_mask = {msd_mask}")
    print("\n\n#######\nI.E. msd_mask HAS SAME NUMBER OF DIGITS AS THE INPUT. THIS IS INTUITION.")
    print("SO // GIVES US THE FIRST DIGIT. AND %= REMOVES THE FIRST DIGIT. \n\n")
    
    loop_counter=0
    for i in range(num_digits // 2):
        loop_counter += 1
        print(f"\n################################################# Loop number: {loop_counter}")
        print(f"Updated msd_mask for loop {loop_counter} = {msd_mask}")
        print(f"Updated x for loop {loop_counter} = {x}")

        print(f"\n###\nFIRST digit = \n x //  msd_mask = {x // msd_mask}")
        print(f"\n###\nLAST digit = \n x % 10 = {x % 10}")
        
        if x // msd_mask != x % 10:         # CHECK FOR PALINDROME.
            return False
        x %= msd_mask  # Remove the most significant digit of x.
        print(f"x after remove MSD i.e. x %= msd_mask = {x}")
        x //= 10  # Remove the least significant digit of x.
        print(f"x after remove LSD = i.e. x //= 10 ={x}")
        msd_mask //= 100
    return True

print(f"is_palindrome_number 33 = {is_palindrome_number(33)}")
print(f"is_palindrome_number 31 = {is_palindrome_number(31)}")
print(f"is_palindrome_number 12321 = {is_palindrome_number(12321)}")
print(f"is_palindrome_number -33 = {is_palindrome_number(-33)}")
