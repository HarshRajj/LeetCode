class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = [nums[i], i]
        nums.sort()
        nums = nums[-k:]
        nums.sort(key= lambda x: x[1])
        res = []
        for i in range(k):
            res.append(nums[i][0])

        return res

            