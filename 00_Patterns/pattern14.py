"""Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:



5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
"""


class Solution:
    def pattern21(self, n):
        size = 2*n - 1
        
        for i in range(size):
            for j in range(size):
                
                top = i
                left = j
                bottom = size - 1 - i
                right = size - 1 - j
                
                min_dist = min(top, left, bottom, right)
                
                print(n - min_dist, end=" ")
            
            print()
# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    obj.pattern21(n) 