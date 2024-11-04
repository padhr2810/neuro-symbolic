"""
TRICK 1: QUOTIENT IS MORE PERMISSIVE THAN 4_5_PRODUCT COZ WE CAN USE "-=" AND "+="
TRICK 2: START AT MASSIVE POWER E.G. 32, IF IT'S LESS THAN X, ADD THE MULTIPLIER TO THE ANSWER '+='
I.E. ADD THIS TO THE ANSWER: ( 1 << POWER ) ..... AND SUBTRACT THE "Y TO BIG POWER" FROM THE X VALUE
TRICK 3: KEEP WORKING BACKWARDS FROM THE BIGGER POWER TO THE SMALLER, AND DO SIMILAR CHECK FOR EACH ONE.
BUT OBVIOUSLY ONLY CHECK AGAINST THE SMALLER VERSION OF X I.E. AFTER SUBTRACTING AS APPROPRIATE.

"""

def divide(x: int, y: int) -> int:
    print(f"\n\n##########################################################################################")
    print(f"\n##############################\nDIVISION {x} / {y}")
    print(f"x {bin(x)}, y {bin(y)}")
    result, power = 0, 32
    y_power = y << power
    print(f"\ny_power = {bin(y_power)}")
    outer_loop_counter = 0 
    while x >= y:
        outer_loop_counter += 1
        print(f"\n######################################################################")
        print(f"OUTER LOOP COUNTER: {outer_loop_counter}\n######################\n")
        print(f"x {bin(x)}, y {bin(y)}")
        inner_loop_counter=0
        while y_power > x:
            inner_loop_counter+= 1
            print(f"\n######################\nINNER LOOP COUNTER: {inner_loop_counter}\n######################\n")

            y_power >>= 1
            print(f"\nShifted y_power = {bin(y_power)}")
            power -= 1
            print(f"\nupdated power = {power}")

        result += 1 << power
        print(f"intermediate result = {result}")
        x -= y_power
        print(f"revised x = {bin(x)}")

    return result

print(f"4 / 2 = {divide(4,2)}")
print(f"5 / 2 = {divide(5,2)}")
print(f"10 / 2 = {divide(10,2)}")
