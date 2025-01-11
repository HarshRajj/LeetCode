class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        ans = [i for i in range(1,n//2+1) if n%i == 0] 
        ans.append(n)
        return ans[k-1] if k-1 < len(ans) else -1
        