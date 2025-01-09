class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xr = 0
        for i in nums:
            xr^=i
        return xr
        