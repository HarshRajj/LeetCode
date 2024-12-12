class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums1)
        b = Counter(nums2)
        ans = []
        c ={}
        for i in a.keys():
            c[i] = min(a[i],b[i])
        
        for k , cnt in c.items() :
            ans.extend([k]*cnt)
        return ans

        
        