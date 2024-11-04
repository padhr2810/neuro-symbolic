
"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
    
        ### TRICK: 2 POINTERS AT OPPOSITE ENDS OF THE STRING
        ###        1 GOES FORWARDS, 1 GOES BACKWARDS.
        ###        MAIN WHILE LOOP SIMPLY CHECKS IF THE POINTERS MET 
        ###        NEED THE SAME CHECK WITHIN 2 INNER WHILE LOOPS, ALSO CHECK FOR VOWELS.
        ###        CAN'T ASSIGN TO STRING USING [i] SO NEED TO CONVERT TO LIST, THEN BACK TO STR AT THE END.
        
        vowels = "aeiouAEIOU"
        
        i, j = 0, len(s) - 1        ### pointers - forwards and backwards
        res_list = list(s)
        while i < j:
            while i < j and res_list[i] not in vowels:      ### similar to palindrome.
                i += 1                                      ### find vowel at start.
             
            while i < j and res_list[j] not in vowels:   ### find vowel at end.
                j -= 1

            if i < j:                              ### check again, not at halfway.
                res_list[i], res_list[j] = res_list[j], res_list[i]        ### swap
                i, j = i + 1, j - 1
        return "".join(res_list)
        
soln = Solution()
input_word = "who is there"
print(soln.reverseVowels(input_word) )
print(soln.reverseVowels("him no") )

assert soln.reverseVowels("hello") == "holle"
assert soln.reverseVowels("leetcode") == "leotcede"
