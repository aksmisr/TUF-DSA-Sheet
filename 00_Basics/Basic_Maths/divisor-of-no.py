"""
You are given an integer n. You need to find all the divisors of n. 
Return all the divisors of n as an array or list in a sorted order.

A number which completely divides another number is called it's divisor.
"""

import math
class Solution:
    def divisors(self, n):
        res = []
        for i in range (1, math.isqrt(n)+1):
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n//i)
        res.sort()
        return(res)
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    divisor = obj.divisors(n)
    print(divisor)

         