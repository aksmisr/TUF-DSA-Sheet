"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

"""


class Solution:
    def pattern20(self, n):
        spaces = 2*n-2
        for i in range(1, 2*n):
            stars = i
            if i>n:
                stars = 2*n-i
            print("*"* stars, end = "")
            print(" "*spaces, end = "")
            print("*"*stars)
            if i<n:
                spaces -=2
            else:
                spaces += 2

# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern20(n) 