"""
Move Zeros to End

Given an integer array nums, move all the 0's to the end of the array. 

The relative order of the other elements must remain the same.



This must be done in place, without making a copy of the array.

"""
class Solution:
    # Function to move zeroes to the end
    def moveZeroes(self, nums):
        # Pointer to the first zero
        j = -1

        # Find the first zero
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        # If no zero found, return
        if j == -1:
            return

        # Start from the next index of first zero
        for i in range(j + 1, len(nums)):
            # If current element is non-zero
            if nums[i] != 0:
                # Swap with nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                # Move j to next zero
                j += 1

# Driver code
sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)

# Print the result
print(" ".join(map(str, nums)))
