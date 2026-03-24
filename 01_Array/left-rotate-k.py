"""
Given an integer array nums, rotate the array to the left by one.



Note: There is no need to return anything, just modify the given array.

"""

def solve(arr, n):
    temp = [0] * n 

 
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]  
  
    for num in temp:
        print(num, end=" ") 
    print()


