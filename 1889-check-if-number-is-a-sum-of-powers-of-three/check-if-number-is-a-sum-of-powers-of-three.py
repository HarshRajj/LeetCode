class Solution:
    def checkPowersOfThree(self, n: int) -> bool:


        ''' 
        chk = [0]
        while ( n > 2) : 
            
            x = int( math. log (n , 3 ))
            if x>16 :
                return False 
            if chk[0] == x:
                return False
            else :
                chk[0] = x
            t = int(math.pow(3,x)) 
            n = n-t 

        return n==1 or n==0
            
        ''' 
        while n > 0:
            rem = n % 3
            if rem == 2: 
                return False
            n //= 3 
        return True


                
        