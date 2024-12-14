class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0 
        while(n//5 > 0):
            m = n//5 
            ans+=m
            n = m 

        return ans

        

        
        