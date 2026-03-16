"""
You are given an integer n. You need to check whether it is an armstrong number or not.
Return true if it is an armstrong number, otherwise return false.

An armstrong number is a number which is equal to the sum of the digits of the number, 
raised to the power of the number of digits.
"""

class Solution:
    def isArmstrong(self, n):
        sum = 0
        dup = n
        while(n>0):
            lastd = n % 10 
            sum = sum + (lastd*lastd*lastd)
            n = n // 10
        return sum == dup
# ---- main driver code ----
if __name__ == "__main__":
    n= int(input())
    obj = Solution()
    armstrong = obj.isArmstrong(n)
    print(armstrong)