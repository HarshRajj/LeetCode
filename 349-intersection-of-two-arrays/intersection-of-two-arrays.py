class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myset = set() 
        for i in nums2 :
            if i in nums1 :
                myset.add(i)
        return list(myset)
        