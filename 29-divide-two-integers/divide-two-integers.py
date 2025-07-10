class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == divisor :
            return 1

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        ans = 0
        sign = 1 


        if (dividend < 0 and divisor >0 ) or (dividend>0 and divisor < 0):
            sign = -1 



        n, d = abs(dividend), abs(divisor)    
        while n >= d :
            cnt = 0
            while n > (d << (cnt + 1) ):
                cnt += 1

            n -= d<<cnt 
            ans += 1<<cnt 


        if ans == ( 1 << 31) and sign == 1 :
            return 1 << 31 - 1 

        return sign * ans

            
        