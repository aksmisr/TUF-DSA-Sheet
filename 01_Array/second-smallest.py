class Solution:
    def secondSmallestElement(self, nums):
        if len(nums) < 2:
            return -1
        small = float('inf')
        second_small = float('inf')
        for num in nums:
            if num < small:
                second_small = small 
                small = num 
            elif num < second_small and num != small:
                second_small = num 
        if second_small == float('inf'):
            return -1
        return second_small
    
nums = list(map(int, input().split()))
obj = Solution()
print("Second Smallest:", obj.secondSmallestElement(nums))