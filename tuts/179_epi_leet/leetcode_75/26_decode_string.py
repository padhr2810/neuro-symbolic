
"""
Given an encoded string, return its decoded string.

INPUT:
    k[encoded_string]
    
E.G.:
    INPUT:  "3[a]2[bc]")
        OUTPUT: "aaabcbc"
    
The encoding rule is: k[encoded_string], 
where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; 
there are no extra WHITE SPACES, 
SQUARE BRACKETS are well-formed, etc. 
Furthermore, the original data does NOT CONTAIN ANY DIGITS and that digits are only for those repeat numbers, k. 
    For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        s1, s2 = [], []
        num, res = 0, ''
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                s1.append(num)
                s2.append(res)
                num, res = 0, ''
            elif c == ']':
                res = s2.pop() + res * s1.pop()
            else:
                res += c
        return res

soln = Solution()
assert soln.decodeString(s = "3[a]2[bc]") == "aaabcbc"
assert soln.decodeString(s = "3[a2[c]]") == "accaccacc"
assert soln.decodeString(s = "2[abc]3[cd]ef") == "abcabccdcdcdef"
