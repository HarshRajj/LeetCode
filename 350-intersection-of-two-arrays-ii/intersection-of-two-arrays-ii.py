class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums1)
        b = Counter(nums2)
        ans = []
        
        inter = a & b

        for k , val in inter.items():
            ans.extend([k]*val)
        return ans

        
        