
"""
TRICK #1: 
BASE CASE = IF "num_rings_to_move == 0" ...

TRICK #2: 
To move N disks THERE ARE 3 STEPS:
1. First you move N-1 disks to the intermediate position,
2. Then you move the BOTTOM disk to the DESTINATION,
3. Finally you move the N-1 disks from the intermediate position to the destination.
The code does exactly that.
"""

import functools
from typing import List

import pprint

#from test_framework import generic_test
#from test_framework.test_failure import TestFailure
#from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

IF_ZERO_TRUE_COUNTER = 0 
SECOND_FUNC_COUNTER  = 0

record_of_recursion_calls= []

def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg,
                                  use_peg):
                                  
        global IF_ZERO_TRUE_COUNTER 
        global SECOND_FUNC_COUNTER
        if num_rings_to_move > 0:
    
            #print(f"\n\n\n#####\nStarting FIRST internal call to recursion !!!!!!!!!!!!!!!!!!!!!!!!!")
            #print(f"\npegs = {pegs}")
            #print(f"\nNum rings to move = {num_rings_to_move}")
            record_of_recursion_calls.append(f"FIRST: num_rings_to_move before FIRST func call= {num_rings_to_move}; pegs = {pegs};  Peg order in func = from_peg={from_peg}; to_peg={use_peg}; use_peg={to_peg}; RESULT = {result}")
            
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg,
                                      to_peg)
                                      
            record_of_recursion_calls.append("")
            record_of_recursion_calls.append("       ***** EXIT FIRST")
            record_of_recursion_calls.append("")
            
            #### MOVE OCCURS HERE!!!
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            record_of_recursion_calls.append(f"   *** MAKE THE MOVE -- from_peg={from_peg}; to_peg={to_peg}")
            record_of_recursion_calls.append("")
            
            print(f"\n\n\n#####\n#####\n#####\nStarting SECOND internal call to recursion")
            record_of_recursion_calls.append(f"SECOND: num_rings_to_move before SECOND = {num_rings_to_move}; pegs = {pegs};  Peg order in func = from_peg=use_peg/{use_peg}; to_peg=to_peg/{to_peg}; use_peg=from_peg/{from_peg}; RESULT = {result}")
            SECOND_FUNC_COUNTER+= 1
            print(f"SECOND_FUNC_COUNTER = {SECOND_FUNC_COUNTER}")

            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg,
                                      from_peg)
            record_of_recursion_calls.append("")
            record_of_recursion_calls.append("       ***** EXIT SECOND")
            record_of_recursion_calls.append("")
                                      
        else:
            record_of_recursion_calls.append("                    ********** EXITED A RECURSION --- num_rings_to_move == 0")
            record_of_recursion_calls.append("")
            IF_ZERO_TRUE_COUNTER += 1
            print(f"\n\nIF_ZERO_TRUE_COUNTER = {IF_ZERO_TRUE_COUNTER}")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            pass
            
    # Initialize pegs.
    result: List[List[int]] = []
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    print(f"\n\n***** Summary of process ***** ")
    for x in record_of_recursion_calls:
        print(x)
    print(f"\nresult = {result}")
    return result


if __name__ == "__main__":
    compute_tower_hanoi(2)

exit()
@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
