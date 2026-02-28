"""Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""


class Solution:
    def pattern(self, n):
        for i in range(n):
            for s in range(n-i-1):
                print(" ", end = "")
            for j in range(i+1):
                print(chr(65+j), end = "")
            for j in range(i-1, -1, -1):
                print(chr(65+j), end = "")
            print()
            # ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern(n) 