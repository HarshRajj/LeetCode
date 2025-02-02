class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        k = 0
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                k += 1

        if nums[n-1]>nums[0]:
            k += 1

        return k <= 1 



        