"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""

class Solution:
    def pattern18(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*", end="")
            for j in range(2*i):
                print(" ", end = "")
            for j in range(n-i):
                print("*", end = "")
            print()
        for i in range(n):
            for j in range(i+1):
                print("*", end = "")
            for j in range(2*(n-i-1)):
                print(" ", end = "")
            for j in range(i+1):
                print("*", end = "")
            print()

# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern18(n) 