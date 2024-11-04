"""
TRICK
	1: GENERATE A LIST OF THE CUMULATIVE PROBABILITIES USING "itertools.accumulate()"
	2: GENERATE A RANDOM NUMBER BETWEEN 0 & 1, USING "random.random()" I.E. THIS IS EQUIVALENT TO A PROBABILITY.
	3: COMPARE #1 & #2. I.E. THE RANDOM NUMBER GENERATED IN #2, IN WHICH INTERVAL DOES IT LIE IN THE ARRAY IN #1
	4: RETURN THE VALUE THAT CORRESPONDS TO THE INDEX OF INTERVAL IN ARRAY #1.
"""

import bisect
import collections
import functools
import itertools
import math
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook


def nonuniform_random_number_generation(values: List[int],
                                        probabilities: List[float]) -> int:

    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
    return values[interval_idx]


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda: [
            nonuniform_random_number_generation(values, probabilities)
            for _ in range(N)
        ])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'nonuniform_random_number.py', 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
