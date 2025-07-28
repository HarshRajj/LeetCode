        
        
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        summ = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                
                seen.remove(nums[left])
                summ -= nums[left]
                left += 1
                
            seen.add(nums[right])
            summ += nums[right]
            max_sum = max(max_sum, summ)
        
        return max_sum