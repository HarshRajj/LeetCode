class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
               
        
        
        def C2(x: int) -> int:
            return (x * (x - 1) // 2) if x >= 2 else 0

        total = (n+2)*(n+1)//2 
        x1 = n - limit + 1    
        t1 = C2(x1)

        x2 = n - 2 * limit     
        t2 = C2(x2)        

        x3 = n - 3 * limit - 1 
        t3 = C2(x3)            

        
        return total - 3 * t1 + 3 * t2 - t3