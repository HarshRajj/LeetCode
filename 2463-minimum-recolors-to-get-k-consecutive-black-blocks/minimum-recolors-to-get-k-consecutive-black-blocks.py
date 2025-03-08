class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blkcnt = 0 
        ans = float('inf')
        for i in range(len(blocks)):
            if i-k >= 0 and blocks [i-k] == 'B' :
                blkcnt -= 1
            if blocks [i]  == 'B' :
                blkcnt += 1
            ans = min(ans, k-blkcnt) 

        return ans

        