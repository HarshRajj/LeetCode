class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxlen = 1
        ln = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                ln += 1
                maxlen = max(maxlen, ln)
            else:
                ln = 1
        ln = 1
        for i in range(1,n):
            if nums[i] < nums[i-1] :
                ln += 1 
                maxlen = max(maxlen, ln)
            else:
                ln = 1

        return maxlen

        