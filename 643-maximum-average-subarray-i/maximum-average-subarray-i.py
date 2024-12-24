class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subSum = sum(nums[:k])
        maxSum = subSum

        for i in range(k, len(nums)):
            subSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, subSum)

        return maxSum / k


        