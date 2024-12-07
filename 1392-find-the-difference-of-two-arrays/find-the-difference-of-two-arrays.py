class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=[]
        b=[]
        s1 = set(nums1)
        s2 = set(nums2)
        for i in s1:
            if i not in s2 :
                a.append(i)
        for i in s2:
            if i not in s1:
                b.append(i)
        return [a,b]
            

        