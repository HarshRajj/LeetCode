class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9+7
        ans = 0
        for q in queries :
            for i in range(q[0], q[1]+1, q[2]) :
                nums[i] *= q[3] % MOD

        for k in nums:
            ans ^= k % MOD

        return ans
        