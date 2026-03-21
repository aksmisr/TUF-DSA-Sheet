"""
Left Rotate Array by One

Given an integer array nums, rotate the array to the left by one.



Note: There is no need to return anything, just modify the given array.

"""

def rotate(nums):
    first = nums[0]         
    
    for i in range(len(nums) - 1):
        nums[i] = nums[i + 1]  
    
    nums[-1] = first        

n = int(input())                     # size of array
nums = list(map(int, input().split()))  # input elements

rotate(nums)

print(*nums)   # print updated array