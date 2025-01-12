class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        '''
        sum1 = 0 
        sum2 = 0
        for i in range(1,n+1):
            if i%m == 0 :
                sum2+=i 
            else :
                sum1+=i 

        return sum1-sum2 
        ''' 

        toto = n*(n+1)//2 
        k = n//m  #k is number of terms divisible by m in range [1,n] 
        divsum = k*m*(k+1)//2 # using sum of N terms of an A.P for multiples of m
        
        num1 = toto-divsum 
        num2 = divsum
        return num1-num2 

        