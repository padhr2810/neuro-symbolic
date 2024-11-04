
"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        ### TRICK: WHILE LOOP CHECKS THAT DIDN'T TRAVERSE TO END OF BOTH STRINGS.
        ###         SEPARATE 'IF' STATEMENTS INTERNALLY, TO KEEP PROGRESSING THROUGH BOTH.
        ###         CAN USE THE USUAL [i] INDEXING TO ACCESS CHARACTERS IN STRING, NO NEED FOR A LIST.
        
        m=len(word1)
        n=len(word2)
        i=0
        j=0
        result=[]
        while i<m or j<n:
            if i<m:
              result+=word1[i]
              i+=1
            if j<n:
                result+=word2[j]
                j+=1
        return "".join(result)


soln = Solution()
x = soln.mergeAlternately("ACE", "BDF")
print(x)
x = soln.mergeAlternately("ACE", "BDFGHI")
print(x)
x = soln.mergeAlternately("1356", "24")
print(x)