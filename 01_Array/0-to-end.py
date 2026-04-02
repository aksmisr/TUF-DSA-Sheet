"""
Move Zeros to End

Given an integer array nums, move all the 0's to the end of the array. 

The relative order of the other elements must remain the same.



This must be done in place, without making a copy of the array.

"""
class Solution:

    def moveZeroes(self, nums):

        j = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        if j == -1:
            return

   
        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)


print(" ".join(map(str, nums)))

"""              Time Complexity        :          O(n)                  
                 Space Complexity       :          O(1)        """
