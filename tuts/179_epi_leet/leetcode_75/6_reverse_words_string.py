
"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
    
        ### TRICK - SIMPLE ONE LINER.
        
        return ' '.join(reversed(s.split()))
    
soln = Solution()

assert soln.reverseWords("the sky is blue") == "blue is sky the"
assert soln.reverseWords("  hello world  ") == "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

assert soln.reverseWords("a good   example") == "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
