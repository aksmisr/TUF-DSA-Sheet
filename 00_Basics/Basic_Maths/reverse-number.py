"""
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.


Example 1

Input: n = 25

Output: 52

Explanation: Reverse of 25 is 52.

Example 2

Input: n = 123

Output: 321

Explanation: Reverse of 123 is 321.
"""

class Solution:
    def reverseNumber(self, n):
        revNo = 0
        while(n>0):
            lastd = n % 10 
            revNo = (revNo *10) + lastd
            n = n // 10
        return revNo
if __name__ == "__main__":
    n = int(input())   
    obj = Solution()
    reverse = obj.reverseNumber(n)
    print(reverse)