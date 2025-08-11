class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Get all powers of two from binary representation of n
        powers = []
        bit = 0
        while n > 0:
            if n & 1:
                powers.append((1 << bit) % MOD)
            bit += 1
            n >>= 1
        
        ans = []
        for left, right in queries:
            prod = 1
            for i in range(left, right + 1):
                prod = (prod * powers[i]) % MOD
            ans.append(prod)
        
        return ans
