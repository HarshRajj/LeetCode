class Solution:
    def isHappy(self, n: int) -> bool:

        if n==1 or n == 7 : return True 
        elif n< 10 : return False 
        else :
            sum = 0 
            while n>0 :
                r = n%10 
                sum += r*r 
                n //= 10

            return self.isHappy(sum)

        