class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        n = len(nums)
        left = [0]*n
        left[0]+= nums[0]
        cnt = 0
        for i in range(1, n):
            left[i] = nums[i]+ left[i-1]

        for i in range(n-1) :
            if left[i] >= totalsum-left[i] :
                cnt += 1

        return cnt


        