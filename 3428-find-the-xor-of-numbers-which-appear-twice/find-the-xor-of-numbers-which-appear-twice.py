class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:

        cnt = Counter(nums) 
        xr = 0
        for k in cnt.keys() :
            if cnt[k]==2 :
                xr = xr^k 

        return xr

