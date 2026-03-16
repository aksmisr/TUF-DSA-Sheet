"""
Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.



Please note that this section might seem a bit difficult without prior knowledge on what hashing is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!


Example 1

Input: nums = [1, 2, 2, 3, 3, 3]

Output: 3

Explanation: The number 3 appears the most (3 times). It is the most frequent element.

Example 2

Input: nums = [4, 4, 5, 5, 6]

Output: 4

Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.
"""

from collections import defaultdict
class Solution:
    def mostFrequentElement(self, nums):
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        max_freq = 0
        ans = float('inf')
        for num, count in freq.items():
            if count > max_freq:
                max_freq = count
                ans = num
            elif count == max_freq:
                ans = min(ans, num)
        return ans
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    sol = Solution()
    result = sol.mostFrequentElement(nums)
    print(result)