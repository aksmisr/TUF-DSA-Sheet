"""Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



1 

0 1 

1 0 1 

0 1 0 1 

1 0 1 0 1
"""

class Solution:
    def pattern11(self, n):
        for i in range(1, n + 1):
            # Decide starting number
            if i % 2 == 1:
                num = 1
            else:
                num = 0
            
            for j in range(i):
                print(num, end=" ")
                # Toggle between 1 and 0
                num = 1 - num
            print()



# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern11(n) 