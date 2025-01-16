class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        x1 = 0
        x2 = 0

        if n1%2 == 0 and n2 % 2 == 0 :
            return 0 

        if n1 % 2 != 0 :
            for i in nums2:
                x2 ^= i

        if n2 % 2 != 0:
            for i in nums1:
                x1 ^= i 

        return x1^x2 

        