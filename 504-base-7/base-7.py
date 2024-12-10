class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        if -7 < num < 7 :
            return str(num)
        m = abs(num)
        while (m > 0):
            ans += str (m%7)
            m //= 7 
        
        if num<0 :
            ans = "-"+ans[::-1]
        else :
            ans = ans[::-1]
        return ans

        
            
        



        