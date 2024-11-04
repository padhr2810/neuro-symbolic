
"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into 
        another EXISTING character, AND do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string AS MANY TIMES as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

"""

from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        # TRICK: BOTH MUST HAVE EXACTLY THE SAME LETTERS- IF ONE ARRAY HAS A DIFFERENT LETTER, FAIL !
        #           I.E. COUNTER KEYS.
        #        AND BOTH SAME LENGTH OBVIOUSLY.
        #        AND BOTH SAME QUANTITIES OF LETTERS WITHOUT WORRYING ABOUT WHICH LETTERS HAVE WHICH QUANTITIES !
        #           I.E. COUNTER VALUES.
       
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return (
                sorted(cnt1.values()) 
                    == 
                      sorted(cnt2.values()) 
                and 
                set(cnt1.keys())
                    == 
                      set(cnt2.keys())
                ) 
                
soln = Solution()

######################################### FALSE:
assert soln.closeStrings(word1 = "abc", word2 = "def") == False
assert soln.closeStrings(word1 = "abc", word2 = "abf") == False
assert soln.closeStrings(word1 = "aabbcc", word2 = "aaabbc") == False 
assert soln.closeStrings(word1 = "a", word2 = "aa") == False
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.


######################################### TRUE: 

assert soln.closeStrings(word1 = "abc", word2 = "bca") == True
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

assert soln.closeStrings(word1 = "aab", word2 = "bba") == True 


assert soln.closeStrings(word1 = "cabbba", word2 = "abbccc") == True 
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
