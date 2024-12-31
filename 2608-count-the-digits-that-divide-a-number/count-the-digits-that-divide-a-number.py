class Solution:
    def countDigits(self, num: int) -> int:
        m = num
        ans = 0 
        while m>0 :
            last = m%10 
            if num % last == 0 :
                ans+=1 
            m//=10

        return ans


        