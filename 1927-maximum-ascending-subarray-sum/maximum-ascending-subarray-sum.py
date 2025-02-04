class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        n = len(nums)
        su = nums[0]
        maxi = su
        for i in range(1,n):
            
            if nums[i]>nums[i-1]:
                su += nums[i]
                maxi = max(su, maxi)
                
            else:
                su = nums[i]
                maxi = max(su, maxi)
                

        return maxi
        