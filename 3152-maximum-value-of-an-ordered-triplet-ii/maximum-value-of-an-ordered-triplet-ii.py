from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0 
        
        premax = [0] * n
        sufmax = [0] * n

        
        premax[0] = nums[0]
        for i in range(1, n):
            premax[i] = max(nums[i], premax[i - 1])

        
        sufmax[n - 1] = nums[n - 1]
        for k in range(n - 2, -1, -1):
            sufmax[k] = max(nums[k], sufmax[k + 1]) 

        maxi = 0
        for j in range(1, n - 1):
            val = (premax[j - 1] - nums[j]) * sufmax[j + 1]
            maxi = max(maxi, val)  

        return maxi
