"""
TRICK: PUT LAST DIGIT AT THE START. AND AT THE NEXT ITERATION, SHIFT IT BACK 1 PLACE USING *10
"""

def reverse(x: int) -> int:
    print(f"\n\n#################################################################################################")
    print(f"REVERSE: x {x} {bin(x)}")
    result, x_remaining = 0, abs(x)
    loop_counter = 0
    while x_remaining:
        loop_counter += 1
        print(f"\n###\nLoop number: {loop_counter}")
        print(f"x_remaining = {x_remaining}")
        result = result * 10 + x_remaining % 10
        print(f"result = {result}")
        x_remaining //= 10
    return -result if x < 0 else result

print(f"reverse 2 = {reverse(2)}")
print(f"reverse 20 = {reverse(20)}")
print(f"reverse 21 = {reverse(21)}")
print(f"reverse 321 = {reverse(321)}")
