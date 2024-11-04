
"""
APPROACH #1 = PYTHONIC WAY BELOW = NOT RECURSIVE, BUT MUCH SIMPLER.
TRICK #1: 
I.E. INITIALISE WITH EMPTY LIST INSIDE A LIST, THIS IS FIRST RESULT.
THEN JUST ITERATE THRU ITEMS IN INPUT_LIST, EACH TIME APPEND USING A LIST COMPREHENSION.

TRICK #2: L1 + L2 
THIS GETS USED TWICE IN ONE LINE BELOW (I.E. ONCE INSIDE THE LIST COMPREHENSION, ONCE BEFORE IT)
ADDING LISTS TO EACH OTHER ... ie. L1 += L2 ...  IS IDENTICAL TO "EXTEND" [BUT NOT "APPEND"] 
CONCISE WAY TO ATTACH NEW ITEMS (FROM LIST COMP) TO AN EXISTING POWER SET. 
NOTE: ONLY WORKS FOR 2 LISTS, DOESN'T WORK FOR LIST AND STRING. WHEREAS "APPEND" OR "EXTEND" WORKS FOR LIST AND STRING.
SO IF APPLYING TO A STRING, NEED TO ENCLOSE THE STRING IN SQUARE BRACKETS I.E. L1 + [S1] 

TRICK #3: PYTHONIC APPROACH USES 2x LOOPS. OUTER LOOP = OVER THE INPUTS. INNER LOOP = OVER THE POWER SET RESULTS TO DATE, THE 2ND LOOP IS INSIDE THE LIST COMPREHENSION.

APPROACH #2 = RECURSIVE WAY.
TRICK #1 = 
TRICK #2 = 
TRICK #3 = 
TRICK #4 = 
"""

from typing import List

def get_power_set_ALSWEIGART(chars):

    if chars == "":     ## BASE CASE.
        return [""]
    
                        ## RECURSIVE CASE.
                        
    powerSet = []       ## STEP 1:INITIALISE powerSet, tail, head.
    head = chars[0]
    tail = chars[1:]
    
                        ## STEP 2: GET SETS WITHOUT THE HEAD.
    tailPowerSet = get_power_set_ALSWEIGART(tail)
    
                        ## STEP 3: APPEND HEAD ITEM ONTO EACH SET WITHOUT HEAD, PUT ALL IN powerSet 
    for tailSet in tailPowerSet:
        powerSet.append(head + tailSet)
    
                        ## STEP 4: EXTEND THE 2 POWER SETS, WITH AND WITHOUT THE HEAD CHARACTER.
    powerSet += tailPowerSet 
    return powerSet 

x=get_power_set_ALSWEIGART("abc")
print(x)
print(len(x)) 
exit() 
# from test_framework import generic_test, test_utils

counter = 0
def generate_power_set(input_set: List[int]) -> List[List[int]]:

    # Generate all subsets whose intersection with input_set[0], ...,
    # input_set[to_be_selected - 1] is exactly selected_so_far.
    def directed_power_set(to_be_selected, selected_so_far):
        global counter, recursive_depth
        counter += 1        
        print(f"\n###\nStarting function ... #{counter}")

        print(f"### to_be_selected ... {to_be_selected} ... selected_so_far ... {selected_so_far}")
        print(f"### Len power_set = {len(power_set)} ... power_set = {power_set}\n")

        if to_be_selected == len(input_set):
            power_set.append(selected_so_far)
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        # Generate all subsets that contain input_set[to_be_selected].
        directed_power_set(to_be_selected + 1,
                           selected_so_far + [input_set[to_be_selected]])

    power_set: List[List[int]] = []
    directed_power_set(0, [])
    return power_set


# Pythonic solution
def generate_power_set_pythonic(S):
    power_set = [[]]
    for a in S:
        power_set += [s + [a] for s in power_set]
    return power_set


if __name__ == '__main__':
    """
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
    """
    generate_power_set(["0", "1", "2", "3"])
    pass 