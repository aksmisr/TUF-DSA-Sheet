"""Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:



*********
 *******
  *****
   ***
    *
"""



class Solution:
    def pattern8(self, n):
        for i in range(n):
            print(" "*i + "*" * (2*(n - i) - 1) )




# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern8(n)