"""
TRICK:
IF DON'T HAVE PRECOMPUTED ANSWERS, CAN DO THIS BY READING FROM THE LSB OF INPUT, THEN AT EACH ITERATION PUSH TO THE LEFT IN RESULT.
"""

##### METHOD 1: BRUTE FORCE
#         BASED ON 4.2 


##### METHOD 2: ARRAY LOOKUP TABLE FOR VERY FAST LOOK UP
#          ILLUSTRATIVE EXAMPLE WITH 8-BIT INTS AND 2-BIT LOOKUP TABLE KEYS.
#          TABLE IS "rev = ((00), (10), (01), (11))"
#          FOR INPUT = (10010011), REVERSE IS: rev(11), rev(00), rev(01), rev(10)

def reverse_bits(x: int) -> int:
    mask_size = 16
    bit_mask  = OxFFFF
    print(f"\nbit_mask = {bit_mask}")
    
    print(f"\nx & bit_mask = {x & bit_mask}")
    print(f"\n3 * mask_size = {3 * mask_size}") 
    print(f"\nx >> mask_size = {x >> mask_size}") 
    print(f"(x >> mask_size) & bit_mask = {(x >> mask_size) & bit_mask}")
    print(f"\n2 * mask_size = {2 * mask_size}") 
    print(f"\nx >> (2 * mask_size) = {x >> (2*mask_size)}") 
    print(f"\n(x >> (2 * mask_size)) & bit_mask = {(x >> (2*mask_size)) & bit_mask}") 
    print(f"\n3 * mask_size = {3 * mask_size}") 
    print(f"\n(x >> (3 * mask_size)) = {(x >> (3 * mask_size))}") 
    print(f"\n(x >> (3 * mask_size)) & bit_mask  = {(x >> (3 * mask_size)) & bit_mask }") 

    return (PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size) |  \
                PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << \
                    (2 * mask_size) | \
                        PRECOMPUTED_REVERSE[(x >> (2 * mask_size)) & bit_mask] << mask_size  | \
                            PRECOMPUTED_REVERSE[(x >> (3 * mask_size)) & bit_mask])
                            
