class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        score = 0
        visited = [False] * n  
        
        for i in sorted(range(n), key=lambda x: nums[x]):
            if not visited[i]:
                score += nums[i]
                visited[i] = True
                
                if i > 0:
                    visited[i - 1] = True
                if i < n - 1:
                    visited[i + 1] = True

        return score
        
    
        