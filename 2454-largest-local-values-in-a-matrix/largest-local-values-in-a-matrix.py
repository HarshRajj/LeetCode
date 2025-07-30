from typing import List

class Solution:
  def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    ans = []
    l = 0
    
    
    while l < n - 2:  # Loop until l can no longer be the start of a 3-unit row
        k = 0
        while k < n - 2:  # Loop until k can no longer be the start of a 3-unit column
            maxi = 0  # Start with 0 (or grid[i][j]) instead of -1
            for i in range(l, l + 3):
                for j in range(k, k + 3):
                    maxi = max(maxi, grid[i][j])
            ans.append(maxi)
            k += 1  
        l += 1  
            
    
    res = [[0] * (n - 2) for _ in range(n - 2)]
    
    
    for i in range(n - 2 - 1, -1, -1):
        for j in range(n - 2 - 1, -1, -1):
            res[i][j] = ans.pop()
            
    return res