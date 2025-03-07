class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def sieve (maxi) :
            isprime = [True] * (maxi + 1) 
            isprime[0] = isprime[1] = False 
            for i in range( 2, int(maxi**0.5) + 1) :
                if isprime[i] :
                    for j in range ( i*i , maxi+1 , i) :
                        isprime[j] = False 
            return isprime 


        isprime = sieve (right) 
        primes = [i for i in range (left, right + 1 ) if isprime[i]] 

        if len(primes) < 2 :
            return [-1,-1] 

        closestpair = [primes[0] , primes[1]] 
        for i in range (len(primes) -1 ) :
            if primes[i+1] - primes[i] < closestpair[1]- closestpair[0] :
                closestpair = [primes[i] , primes[i+1]] 

        return closestpair
        