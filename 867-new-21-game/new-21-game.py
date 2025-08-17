class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        if n < k:
            return 0.0
        dp = [0.0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = 1.0
        right = min(n, k + maxPts - 1)
        window = sum(dp[k: right + 1])

        for i in range(k - 1, -1, -1):
            dp[i] = window / maxPts
            window += dp[i]
            if i + maxPts <= n:
                window -= dp[i + maxPts]

        return dp[0]