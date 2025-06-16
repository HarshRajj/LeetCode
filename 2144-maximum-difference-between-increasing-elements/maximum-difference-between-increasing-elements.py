class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = nums[0] 
        maxdiff = -1

        for i in range(1, len(nums)) :
            if nums[i] <= mini :
                mini = nums[i] 
            else :
                maxdiff = max(maxdiff, (nums[i] - mini))

        return maxdiff
            

        