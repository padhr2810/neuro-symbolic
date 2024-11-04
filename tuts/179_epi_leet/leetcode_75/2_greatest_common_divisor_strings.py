
"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that 
x divides both str1 and str2.
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        ### TRICK: FUNCTION TO CHECK EACH SUBLEN.
        ###        LOOP FROM SMALLEST str DOWN TO ZERO - CALLING THE FUNC EACH TIME.
        ###        COMMON DIVISOR -- IMPLIES BOTH STR START WITH SAME CHAR (OTHERWISE FAIL).
        ###        MULTIPLY PART OF str1 AND CHECK IF == str1 AND str2. DON'T MULTIPLY ANY PART OF "str2"
        
        len1, len2 = len(str1), len(str2)
        print(f"str1 = {str1}; str2 = {str2}")
        print(f"len1 = {len1}; len2 = {len2}")
        
        def isDivisor(sublen):
            ##### 1: ensure % = 0 (i.e. no remainder)
            ##### 2: store number of times sublen divides into s1 and s2.
            ##### 3: multiply result of 2 by first 'sublen' chars of s1 or s2. Return true or false.
            
            print(f"\n\nlen1 % sublen = {len1 % sublen}")
            print(f"len2 % sublen = {len2 % sublen}")
            
            if len1 % sublen or len2 % sublen:      #### DOESN'T DIVIDE SO TRY NEXT NUMBER.
                return False
                
            print(f"len1 // sublen = {len1 // sublen}")
            print(f"len2 // sublen = {len2 // sublen}")
            
            f1, f2 = len1 // sublen , len2 // sublen    ### CHECK HOW MANY TIMES IT DIVIDES IN.
            
            print(f"str1[:sublen] * f1 = {str1[:sublen] * f1}")
            print(f"str1[:sublen] * f2 = {str1[:sublen] * f2}")
            
                                  ##### LOGIC: MULTIPLY PART OF "str1" TO GET FULL "str1" AND ALSO "str2"
            return str1[:sublen] * f1 == str1 and str1[:sublen] * f2 == str2
            
        for sublen in range(min(len1, len2), 0 , -1):  
            if isDivisor(sublen):
                return str1[:sublen]    ### COULD ALSO RETURN str2[:sublen] AS IT'S THE SAME.
        return ""

soln = Solution()
x = soln.gcdOfStrings("ABABAB", "ABAB")
print(x)

assert soln.gcdOfStrings("ABCABC", "ABC") == "ABC"
assert soln.gcdOfStrings("ABABAB", "ABAB") == "AB"
assert soln.gcdOfStrings("LEET", "CODE") == ""
assert soln.gcdOfStrings("LEET", "EET") == ""

