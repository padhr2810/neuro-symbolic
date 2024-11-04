"""
TRICK:
CREATE AN "ADD()" FUNCTION FIRST, DON'T GO STRAIGHT FOR MULTIPLY().
ADD() BY CONSIDERING 2 ASPECTS, 1: THE CARRY (I.E. & ) AND 2: THE SIMPLE ADD WHERE CARRY IS NOT NEEDED I.E. | 
THEN WILL JUST USE THIS ADD() WHENEVER X&1, OBVIOUSLY WILL X>>=1 AND Y<<=1 TO HANDLE THE MORE SIGNIFICANT BITS.
I.E. ONLY CONSIDER THE FINAL BIT OF 'X' IN EACH ITERATION.
"""

def add(a,b):       ### ONLY 2 LINES IN WHILE.
    print(f"\n###################################################\nADDITION OF {a} AND {b}\n###################################################\n")
    print(f"{bin(a)} ... {bin(b)}")
    iter = 1
    while b:        ### I.E. UNTIL GET RID OF CARRY.
        print(f"\n###################################################\niter no. {iter}\n###################################################")
        
        carry = a&b

        print(f"\ncarry = {bin(carry)} ... i.e. a&b")
        print(f"a^b = {a^b}")
        print(f"carry << 1 = {bin(carry << 1)}")

        a,b = a^b, carry << 1

        print(f"\nUpdated a,b = ........... {a,b} ... {bin(a), bin(b)} ..... i.e. a^b, carry << 1")
        iter+=1
    return a 
        
def multiply_non_negatives(x: int, y: int) -> int:
    """
    Enters into an infinit loop if try with a NEGATIVE number!!
    Set up an assert to avoid this.
    """
    
    assert x >= 0   # critical !!
    assert y >= 0
    
    print(f"\n\n##########################\n##########################\n##########################\n")
    print(f"\nInputs x, y = {x, y}")
    print(f"\nbinary x, y = {bin(x), bin(y)}")

    
    running_sum = 0 
    number_of_iterations=1
    while x: 
        print(f"\n########\nIteration = {number_of_iterations}\n########")
        print(f"\nnew x = {x} ... binary {bin(x)}")
        print(f"\nnew y = {y} ... binary {bin(y)}")
        print(f"\nx&1 = {x&1} ... binary {bin(x&1)}")
        if x&1:
            running_sum = add(running_sum,y)
        print(f"\nnew running sum = {running_sum} ... {bin(running_sum)}")
        x,y = x >> 1, y << 1 
        print(f"\nx,y = x >> 1, y << 1 ........... = {x,y}... bin {bin(x), bin(y)}")
        number_of_iterations+=1
    print(f"\nfinal running sum = {running_sum}")
    return running_sum, number_of_iterations

x1_5, iters_1_5 = multiply_non_negatives(1, 5)
x2_5, iters_2_5 = multiply_non_negatives(2, 5)
x11_10, iters_11_10 = multiply_non_negatives(11, 10)
x100_100, iters_100_100 = multiply_non_negatives(100, 100)
x255_255, iters_255_255 = multiply_non_negatives(255, 255)
x1million_1million, iters_1million_1million = multiply_non_negatives(1000000, 1000000)

print(f"1 x 5 = {x1_5} ... bin {bin(1)} * {bin(5)} after {iters_1_5} iterations") 
print(f"2 x 5 = {x2_5} ... bin {bin(2)} * {bin(5)} after {iters_2_5} iterations")
print(f"11 x 10 = {x11_10} ... bin {bin(11)} * {bin(10)} after {iters_11_10} iterations")
print(f"100 x 100 = {x100_100} ... bin {bin(100)} * {bin(100)} after {iters_100_100} iterations")
print(f"255 x 255 = {x255_255} ... bin {bin(255)} * {bin(255)} after {iters_255_255} iterations")
print(f"1 million x 1 million = {x1million_1million} ... bin {bin(1000000)} * {bin(1000000)} after {iters_1million_1million} iterations")

print(f"\n\n############\nCHECK ADDITION\n############\n\n")
print(f"add 2 + 5 = {add(2,5)}")
print(f"add 15 + 15 = {add(15,15)}")
