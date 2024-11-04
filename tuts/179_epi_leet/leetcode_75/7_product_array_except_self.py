"""
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums) :
              ### THE TRICK: FIRST MULTIPLY ALL NUMS TO LEFT. THEN MULTIPLY THE RESULT BY ALL NUMS TO RIGHT.
              ###    SEPARATE LOOPS FOR LEFT AND RIGHT. INIT EACH TO 1.
              ###    "left" LOOP - NEED "enumerate" TO i) ASSIGN TO RESULT ARRAY (using 'i'). ii) PULL THE VAL FROM INPUT
              ###        IN PRINCIPLE COULD DO BOTH OF THESE WITHOUT ENUMERATE, JUST USING "range"
              ###    "right" LOOP - GOES FROM "n-1" TO "-1" TO HIT THE '0' INDEX.
              ###        IF ONLY WENT FROM "n-1" TO "0", IT WOULDN'T REACH '0', WOULD STOP BEFORE IT AT '+1'
              
        n = len(nums)
        ans = [0] * n                   ##### ARRAY OF ZEROES TO HOLD ANSWER.
        left = right = 1
        print(f"\n\n\n###########################\ninput = {nums}")
        
        print("\n\nSTARTING THE FIRST LOOP:")        
        """
        # ENUMERATE METHOD:
        for i, val_i in enumerate(nums):    ### STEP 1: MULTIPLY ALL NUMS TO LEFT.
            ans[i] = left       ### FIRST ASSIGN THE "left" CUMULATIVE VALUE TO THE "ans" ARRAY.
            left *= val_i       ### THEN UPDATE THE LEFT BY MULTIPLYING WITH THE VALUE.
        """
        # RANGE METHOD:
        for i in range(len(nums)):    ### STEP 1: MULTIPLY ALL NUMS TO LEFT.
            ans[i] = left       ### FIRST ASSIGN THE "left" CUMULATIVE VALUE TO THE "ans" ARRAY.
            left *= nums[i]       ### THEN UPDATE THE LEFT BY MULTIPLYING WITH THE VALUE.
        
        
        print(f"\nans after first loop: {ans} \n")
        
        print("\n\nSTARTING THE 2ND LOOP:")
        for i in range(n - 1, -1, -1):      ### STEP 2: MULTIPLY BY ALL NUMS TO RIGHT.
            print(f"i = {i}; ans[i] = {ans[i]}; right = {right}; nums[i] = {nums[i]}")
            ans[i] *= right
            right *= nums[i]
        return ans

soln = Solution() 
assert soln.productExceptSelf(nums = [1,2,3,4]) == [24,12,8,6]
exit()
assert soln.productExceptSelf(nums = [-1,1,0,-3,3]) == [0,0,9,0,0]

