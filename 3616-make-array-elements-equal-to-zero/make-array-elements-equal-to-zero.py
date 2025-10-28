class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        valid = 0
        
        for i, x in enumerate(nums):
            right_sum = total_sum - left_sum
            if x == 0:
                diff = abs(right_sum - left_sum)
                if diff == 0:
                    valid += 2   # both directions possible
                elif diff == 1:
                    valid += 1   # only one direction works
            left_sum += x
        
        return valid