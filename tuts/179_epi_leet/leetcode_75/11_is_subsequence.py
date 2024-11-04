"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string 
that is formed from the original string by deleting some (can be none) of the characters 
WITHOUT disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        
        ### TRICK: MAIN LOOP SIMPLY ENSURES DIDN'T REACH END OF AT LEAST ONE STRING.
        ###     Only advance a step in first array IF EQUAL to 2nd array.
        ###     But always advance a step through the Second array. (irrespective of equal / not equal)
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
        
soln = Solution()
assert soln.isSubsequence(s = "abc", t = "ahbgdc") == True 
assert soln.isSubsequence(s = "axc", t = "ahbgdc") == False 

