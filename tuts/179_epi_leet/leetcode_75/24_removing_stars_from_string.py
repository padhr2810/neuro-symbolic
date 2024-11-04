
"""
You are given a string s, which contains stars *.

In one operation, you can:
- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note: The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
"""

class Solution:
    def removeStars(self, s: str) -> str:
    
        # TRICK: INIT NEW LIST TO HOLD THE RESULTS.
        #           MUST BE LIST (NOT STR) COZ IT'S A STACK (I.E. 'POP' METHOD)
        #        ITERATE THROUGH INPUT
        #           IF STAR THEN POP... OTHERWISE APPEND.
        #        CAVEAT: CODE WOULD FAIL IF STAR AT THE START. BUT THESE INPUTS ARE NOT PERMITTED.
        
        ans = []
        for c in s:
            if c == '*':
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)
        
soln = Solution()

assert soln.removeStars(s = "leet**cod*e") == "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".

assert soln.removeStars(s = "erase*****") == ""
# Explanation: The entire string is removed, so we return an empty string.


