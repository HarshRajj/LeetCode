
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        
        # 1) Sum along the main diagonal
        for i in range(n):
            ans += fruits[i][i]
        
        # Helper: max‐path from top‐right through the “upper‐triangle” region
        def dp() -> int:
            NEG_INF = -10**18
            prev = [NEG_INF] * n
            curr = [0] * n
            
            # start at (0, n-1)
            prev[n - 1] = fruits[0][n - 1]
            
            for i in range(1, n - 1):
                # reset curr row to NEG_INF
                curr = [NEG_INF] * n
                
                # valid range: columns strictly above the diagonal
                start = max(n - 1 - i, i + 1)
                for j in range(start, n):
                    # best from three possible predecessors
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    
                    # add current cell’s fruits
                    curr[j] = best + fruits[i][j]
                
                # swap prev and curr for next iteration
                prev, curr = curr, prev
            
            # end at (n-1, n-1)
            return prev[n - 1]
        
        # 2) Run DP for Child B (upper‐triangle path)
        ans += dp()
        
        # 3) Transpose the upper half of the matrix into the lower half
        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
        
        # 4) Run DP again for Child C (now covering the original lower‐triangle)
        ans += dp()
        
        return ans