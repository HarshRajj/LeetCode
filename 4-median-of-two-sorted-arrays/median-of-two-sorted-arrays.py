from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2  # total number of elements
        ind1 = (n - 1) // 2
        ind2 = n // 2

        ind1el, ind2el = -1, -1
        i, j = 0, 0
        cnt = 0

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                val = nums1[i]
                i += 1
            else:
                val = nums2[j]
                j += 1

            if cnt == ind1:
                ind1el = val
            if cnt == ind2:
                ind2el = val
            cnt += 1

        while i < n1:
            val = nums1[i]
            if cnt == ind1:
                ind1el = val
            if cnt == ind2:
                ind2el = val
            i += 1
            cnt += 1

        while j < n2:
            val = nums2[j]
            if cnt == ind1:
                ind1el = val
            if cnt == ind2:
                ind2el = val
            j += 1
            cnt += 1

        if n % 2 == 1:
            return float(ind2el)
        else:
            return (ind1el + ind2el) / 2

 


        