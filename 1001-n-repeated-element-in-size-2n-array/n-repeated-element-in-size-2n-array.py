class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range (n-1):
            if nums[i] == nums[i+1] : return nums[i]
            if i+2 < n and nums[i] == nums[i+2] : return nums[i]
            if i+3 < n and nums[i] == nums[i+3] : return nums[i]

        return -1



            

        