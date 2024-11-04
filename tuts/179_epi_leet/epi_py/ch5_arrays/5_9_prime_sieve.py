"""
TRICK
CREATE A "BOOLEAN ARRAY". ASSUME FIRST 2 VALUES = FALSE, BUT EVERYTHING ELSE ASSUME "TRUE" (I.E. PRIME) UNTIL PROVE OTHERWISE.
WHENEVER FIND A PRIME: I) APPEND TO PRIMES LIST. II: SIEVE OUT ALL MULTIPLES OF THIS PRIME FROM THE BOOLEAN ARRAY.
2 OPTIMISATIONS: I) ONLY CONSIDER ODD NUMBERS (EVEN CAN'T BE PRIME AFTER 2)
                 II) START THE SIEVE FROM P-SQUARED (INSTEAD OF P) 
                 	BECAUSE ALL MULTIPLES OF P THAT ARE < P-SQUARED WILL ALREAD BE SIEVED OUT IN EARLIER STEP.
                 	I.E. THIS AVOIDS UNNECESSARY DUPLICATION OF PRIME SIEVING. 
                 	E.G. IF 'P' = 7, ALREADY HAVE SIEVED OUT 7*1, 7*2, 7*3, 7*4, 7*5, 7*6 ... SO CAN START SIEVING WITH 7*7
"""

from typing import List

from test_framework import generic_test

def naive_approach(n: int) -> List[int]:
    primes = [] 
    is_prime = [False, False] + [True] * (n-1) 
    for p in range(2, n+1): 
        if is_prime[p]:
            primes.append(p)
            for i in range(p*2, n+1, p):
                is_prime[i] = False 
    return primes 

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:

    if n < 2:
        return []
    size = (n - 3) // 2 + 1		# E.G. IF N=3 OR N=4, THE SIZE FOR CHECKING IS STILL GONNA BE 1 (COZ ONLY CHECK ODD NUMS.. & WE SKIP 0,1,2 HERE)
    primes = [2]  # Stores the primes from 1 to n.
    # is_prime[i] represents (2i + 3) is prime or not.
    # For example, is_prime[0] represents 3 is prime or not, is_prime[1]
    # represents 5, is_prime[2] represents 7, etc.
    # Initially set each to true. Then use sieving to eliminate nonprimes.
    
    is_prime = [True] * size		# SIZE ADJUSTED EARLIER TO ACCOUNT FOR OMITTING EVEN NUMBERS.
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3		# I.E. "i:p" = 0:3  1:5  2:7
            				#     +3 COZ SKIP 0,1,2 ... I.E. FOR INDEX 0, CHECK IF 3 IS PRIME.
            				#     & MULTIPLY X2 COZ WE'RE SKIPPING THE EVEN NUMBERS.
            primes.append(p)
            # Sieving from p^2, where p^2 = (4i^2 + 12i + 9). The index in is_prime
            # is (2i^2 + 6i + 3) because is_prime[i] represents 2i + 3.
            #
            # Note that we need to use long for j because p^2 might overflow.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
