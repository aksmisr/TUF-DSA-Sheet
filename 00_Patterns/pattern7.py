"""Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



ABCDE

ABCD

ABC

AB

A
"""


class Solution:
    def pattern15(self, n):
        for i in range(n):
            for j in range(n-i):
                print(chr(65+j), end = "")
            print()

# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern15(n) 