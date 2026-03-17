"""
Second Largest Element

Given an array of integers nums, return the second-largest element in the array. 
If the second-largest element does not exist, return -1.

"""

class Solution:
    def secondLargestElement(self, nums):
        if len(nums) < 2:
            return -1
        large = float('-inf')
        second_large = float('-inf')
        for num in nums:
            if num > large:
                second_large = large
                large = num
            elif num > second_large and num != large:
                second_large = num
        if second_large == float('-inf'):
            return -1
        return second_large      
    


