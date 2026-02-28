"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



12345

1234

123

12

1"""

class Solution:
    def pattern6(self, n):
        for i in range(n):
            for j in range(1, n-i+1):
                print(j, end = "")
            print()
# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern6(n)

    