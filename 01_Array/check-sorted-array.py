"""

Check if the Array is Sorted II

Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

"""

class Solution:
    def isSorted(self, nums):
        for i in range(1, len(nums)):
            if(nums[i] >= nums[i-1]):
                {

                }
            else:
                return False 
        return True

nums = list(map(int, input().split()))

obj = Solution()
result = obj.isSorted(nums)

print(result)