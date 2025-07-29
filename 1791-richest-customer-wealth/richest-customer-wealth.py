class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0 
        for arr in accounts :
            s = sum(arr)
            maxi = max(maxi, s)
        
        return maxi        