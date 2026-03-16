"""
You are given an integer n. You need to check if the number is prime or not. 
Return true if it is a prime number, otherwise return false.

A prime number is a number which has no divisors except 1 and itself.
"""

class Solution:
    def isPrime(self, n):
        cnt = 0
        for i in range (1, int(n**0.5) + 1):
            if n % i == 0:
                cnt += 1
                if n // i != i:
                    cnt += 1
        return cnt == 2
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    prime = obj.isPrime(n)
    print(prime)