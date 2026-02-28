"""Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



*****
*   *
*   *
*   *
*****
"""


class Solution:
    def pattern21(self, n):
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i == n-1 or j == n-1:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print()
# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern21(n) 