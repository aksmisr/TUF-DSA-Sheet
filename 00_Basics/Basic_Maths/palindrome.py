"""
You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.



A palindrome number is a number which reads the same both left to right and right to left.


Example 1

Input: n = 121

Output: true

Explanation: When read from left to right : 121.

When read from right to left : 121.

Example 2

Input: n = 123

Output: false

Explanation: When read from left to right : 123.

When read from right to left : 321.
"""
class Solution:
    def isPalindrome(self, n):
        revNo = 0
        dup = n
        while(n>0):
            lastd = n % 10 
            revNo = (revNo *10) + lastd
            n = n // 10
        return revNo==dup
if __name__ == "__main__":
    n = int(input())   
    obj = Solution()
    palindrome = obj.isPalindrome(n)
    print(palindrome)