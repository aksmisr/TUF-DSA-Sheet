"""
Largest Element

Given an array of integers nums, return the value of the largest element in the array
"""

class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest
    
nums = list(map(int, input().split()))
obj = Solution()
result = obj.largestElement(nums)
print("Largest element is:", result)
 


"""              Time Complexity        :          O(n)                  
                 Space Complexity       :          O(1)        """