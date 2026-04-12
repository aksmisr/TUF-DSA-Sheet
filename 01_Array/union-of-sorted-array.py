"""

Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.



The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.


Example 1

Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2, 3, 4, 5, 7]

Explanation:

The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2

Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]

Output: [1, 3, 4, 5, 6, 7, 8, 9]

Explanation:

The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2

"""

class Solution:
    def findUnion(self, arr1, arr2, n, m):

        Union = []
        i, j = 0, 0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
            # If element in arr2 is smaller
            elif arr2[j] < arr1[i]:
                if not Union or Union[-1] != arr2[j]:
                    Union.append(arr2[j])
                j += 1
            else:
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
                j += 1
        while i < n:
            if not Union or Union[-1] != arr1[i]:
                Union.append(arr1[i])
            i += 1

        # Append remaining elements from arr2
        while j < m:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])
            j += 1
        return Union

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    n, m = len(arr1), len(arr2)

    obj = Solution()
    result = obj.findUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is:", *result)            


"""              Time Complexity        :          O(m+n                  
                 Space Complexity       :          O(m+n)         """


