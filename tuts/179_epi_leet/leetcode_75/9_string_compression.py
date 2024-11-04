
"""
Given an array of characters, compress it using the following algorithm:

    --- Begin with an empty string s. For each GROUP of consecutive repeating characters in chars:
    --- If the group's length is 1, append the character to s.
    --- Otherwise, append the character followed by the group's length.
    --- The compressed string s should NOT be stored separately, but instead, be STORED IN THE INPUT CHARACTER ARRAY "chars". 
            Note that group lengths that are 10 or longer will be split into multiple characters in chars.

    --- After you are done modifying the input array, RETURN the new LENGTH of the array.

    --- You must write an algorithm that uses only constant extra space.
"""

class Solution:
    def compress(self, chars) -> int:
    
        ### TRICK: USE 2 POINTERS - FAST AND SLOW 
        ###     MAIN LOOP CHECKS IF 'SLOW' REACHED END OF ARRAY
        ###         INTERNAL LOOP -- 1: CHECK IF "FAST" REACHED END OF ARRAY 
        ###                      2: AND CHECKS FOR DUPLICATES - IF YES THEN KEEP PROGRESSING.
        ###     WHEN REACH END OF HOMOGENEOUS GROUP - UPDATE THE START OF STRING WITH THE RESULT.
        ###     COUNTING THE NUMBER HAPPENS BY COMPARISON OF INDICES. [NO NEED TO INCREMENET A COUNTER]
        ###     LOGIC - ADD NUMBER TO ARRAY IF > 1
        ###     AFTER ADD A RESULT --- THE "slow" CATCHES UP WITH "fast"
        
        i_slow, faster_j, len_output, len_input = 0, 0, 0, len(chars)
        while i_slow < len_input:
        
            faster_j += 1
            
            while faster_j < len_input and chars[faster_j] == chars[i_slow]:     ### KEEP PROGRESSING IF DUPLICATES.
                faster_j += 1
            
            chars[len_output] = chars[i_slow]    ##### BRING BACK A CHAR TO FIT INTO THE OUTPUT NUM.
            len_output += 1                      ##### ANOTHER STEP ALONG THE RESULT ARRAY.
            
            if faster_j - i_slow > 1:        ##### LOGIC - ADD NUMBER TO ARRAY IF > 1
                cnt = str(faster_j - i_slow)    #### COUNTING HAPPENS BY COMPARISON OF INDICES.
                for c in cnt:           ##### HERE ADD THE COUNT TO THE ARRAY.
                    chars[len_output] = c
                    len_output += 1
                
            i_slow = faster_j            ##### CATCHUP.
        print(f"revised chars = {chars}")
        return len_output
        
soln = Solution()
assert  soln.compress(chars = ["a","a","b","b","c","c","c"]) == 6 
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

assert  soln.compress(chars = ["a"]) == 1
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.

assert  soln.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

assert  soln.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b", "c"]) == 5
# Output: Return 5, and the first 5 characters of the input array should be: ["a","b","1","2","c"].


