
"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
This assumes all lowercase.
"""


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        ### TRICK: sliding window - just change the first & last values.
        
        vowels = set('aeiou')
        #vowels = 'aeiou'       ### can do it as string or set... same result.
        
        latest_check = sum(c in vowels for c in s[:k])     ### check first 'k' samples.
        ans = latest_check
        for i in range(k, len(s)):
            latest_check += s[i] in vowels      ### sliding window - just change the first & last values.
            latest_check -= s[i - k] in vowels
            ans = max(ans, latest_check)
        return ans
        
        
soln = Solution()
assert soln.maxVowels(s = "abciiidef", k = 3) == 3
# Explanation: The substring "iii" contains 3 vowel letters.

assert soln.maxVowels(s = "aeiou", k = 2) == 2
# Explanation: Any substring of length 2 contains 2 vowels.

assert soln.maxVowels(s = "leetcode", k = 3) == 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
