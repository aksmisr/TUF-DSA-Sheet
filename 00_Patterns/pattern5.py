"""Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



*

**

***

****

*****

****

***

**

*

"""



class Solution:
    def pattern(self, n):
        for i in range(1, n + 1):
            print("*" * i)
        for i in range(n - 1, 0, -1):
            print("*" * i)
# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern(n)
    