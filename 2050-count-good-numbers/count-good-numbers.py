class Solution:
    def power(self,base, exp):
        MOD = 10**9 + 7
        ans = 1 
        while exp > 0:
            if exp%2 == 1:
                ans = ( ans*base ) % MOD
            base = ( base*base ) % MOD
            exp = exp//2 

        return ans

    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even = (n+1)//2 
        odd = n//2 

        return (self.power(5,even)*self.power(4,odd))%MOD


       