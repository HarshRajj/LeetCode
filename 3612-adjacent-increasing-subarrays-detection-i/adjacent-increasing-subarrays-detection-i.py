class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
    
    
        def is_strictly_increasing(i):
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:
                    return False
            return True
    
    
        for i in range(n - 2 * k + 1): 
            if is_strictly_increasing(i) and is_strictly_increasing(i + k):
                return True
        