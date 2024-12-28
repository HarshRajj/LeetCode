class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums) 
        for key in c.keys():
            if c[key]>=2 :
                return key

        