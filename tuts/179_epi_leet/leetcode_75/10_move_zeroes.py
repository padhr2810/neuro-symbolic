
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    # The Trick: EVERY time a non-zero is encountered, it gets "pushed forward"
    #     if no zero encountered yet, the non-zero just gets swapped with itself at each step.
    # Every time encounter a zero, 'i' falls a step behind the 'stepper' so the zero gets swapped with non-zero.
    #     if three zeros in a row, the non-zero gets swapped with the first zero (coz 'i' falls 3 steps behind)
    def moveZeroes(self, nums ) -> None:
        print(f"\n\n###########################################################################")
        print(f"\nInput = {nums}")
        zero_to_swap = 0       ### starts at the same place as stepper, but falls behind every time a zero is found.
        for stepper, x in enumerate(nums):
            if x:
                print("\n     PUSH FORWARD NON-ZERO HAPPENING!!!")
                print(f"zero_to_swap,stepper = {zero_to_swap},{stepper}")  
                print(f"nums[stepper], nums[zero_to_swap] = {nums[stepper], nums[zero_to_swap]}")                
                nums[zero_to_swap], nums[stepper] = nums[stepper], nums[zero_to_swap]
                zero_to_swap += 1      ### zero_to_swap == stepper if no zeroes. i.e. no swap.
                            ###    i.e. swap '0' with next instance of non-zero.
        return nums 
                
soln = Solution()
assert soln.moveZeroes(nums = [0,1,0,3,12]) == [1,3,12,0,0]
assert soln.moveZeroes(nums = [0,1,3,12]) == [1,3,12,0]
assert soln.moveZeroes(nums = [1,3,0,5,6]) == [1,3,5,6,0]
assert soln.moveZeroes(nums = [1,0,0,0,6]) == [1,6,0,0,0]
assert soln.moveZeroes(nums = [0]) == [0]
