"""
TRICK
INPUT ARRAY DOESN'T EXIST IN MEMORY - IT'S JUST HYPOTHETICAL BASED ON A RANGE FROM 0 TO N-1.
CLEVER BIT IS TO SIMULATE THE SOLUTION OF 5.12 WITHOUT ANY ARRAY 'A', 
INSTEAD USE A HASH TABLE (changed_elements) TO INDICATE WHERE VALUES DIFFER FROM INDICES IN THE HYPOTHETICAL INPUT ARRAY.
ITERATE FOR EACH ELEMENT OF THE SUBSET AND ADD THE ADJUSTED VALUES/INDICES OF HYPOTHETICAL INPUT ARRAY 'A' TO THE HASH TABLE ('changed_elements') 

WORKED EXAMPLE: INPUTS: n=100, k=4
ITERATION 1: RANDOM NUMBER 28.
	H = { (0,28}, (28,0) } 
ITERATION 2: RANDOM NUMBER 42
	H = { (0,28}, (28,0), (1,42), (42,1) } 
ITERATION 3: RANDOM NUMBER IS 28 AGAIN. ... THIS IS THE TRICKY BIT... 
	H = { (0,28}, (28,2), (1,42), (42,1), (2,0) } 
ITERATION 4: RANDOM NUMBER IS 64.
	H = { (0,28}, (28,2), (1,42), (42,1), (2,0), (3,64), (64,3) } 
"""

import functools
import random
from typing import Dict, List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def random_subset(n: int, k: int) -> List[int]:

    changed_elements: Dict[int, int] = {}
    for i in range(k):
        # Generate a random index between i and n - 1, inclusive.
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
        print(f"\nIter {i}: rand_idx = {rand_idx}; rand_idx_mapped = {rand_idx_mapped}; i_mapped = {i_mapped}; changed_elements = {changed_elements}")
    return [changed_elements[i] for i in range(k)]

random_subset(50,5)
exit() 

# Pythonic solution
def random_subset_pythonic(n, k):
    return random.sample(range(n), k)


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
