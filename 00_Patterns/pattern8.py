"""Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



A

BB

CCC

DDDD

EEEEE
"""

class Solution:
    def pattern16(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+i), end = "")
            print()
# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern16(n) 