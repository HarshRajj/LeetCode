class Solution:
    def coloredCells(self, n: int) -> int:

        # simple maths : use Arithmetic progressions  --- 
        #  we know that sum of n terms is : S(n) = n/2 [ 2*a + (n-1)*d] 
        #  and nth term is :  t(n) = [ a + (n-1)*d]
        
        snm1 = (n-1) * ( 2 + (n-2) * 2 ) 
        tn = 1 + ( n-1 ) * 2 

        return snm1 + tn 

        