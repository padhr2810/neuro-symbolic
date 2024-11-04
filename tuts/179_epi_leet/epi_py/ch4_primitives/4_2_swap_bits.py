"""
TRICK:
IF THE 2 RESPECTIVE BITS ARE DIFFERENT, THEN USE A BIT MASK TO FLIP THEM USING ^=
"""

def swap_bits(input_value, i, j):

    # Extract the i-th and j-th bits for 1 binary word, and see if they differ.
    print(f"len of input_value as binary: {len(bin(input_value)) }")
    print(f" input_value as binary: {bin(input_value) }")
    print(f" input_value [i]: {bin(input_value)[i] }")
    print(f" input_value [j]: {bin(input_value)[j] }")
    if (input_value >> i) & 1 != (input_value >> j) & 1:
        # i-th and j-th bits differ. We will swap them by flipping their values.
        # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1
        # when x = 0, we can perform the flip XOR.
        
        
        bit_mask = (1 << i) | (1 << j)
        print(f"bit_mask = {bit_mask}")
        
        input_value ^= bit_mask
    # if they don't differ just return the original binary word.
    return input_value


swapped_7_01 = swap_bits(7,0,1)
swapped_6_01 = swap_bits(6,0,1)
swapped_6_02 = swap_bits(6,0,2)
print("#################################################################")
print(f"swapped 7 0_1 / {bin(7)} = {swapped_7_01} / {bin(swapped_7_01) }") 
print(f"swapped 6 0_1 / {bin(6)} = {swapped_6_01} / {bin(swapped_6_01) }") 
print(f"swapped 6 0_2 / {bin(6)} = {swapped_6_02} / {bin(swapped_6_02) }") 
