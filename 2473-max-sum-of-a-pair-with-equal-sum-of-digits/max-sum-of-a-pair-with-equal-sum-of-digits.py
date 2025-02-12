
class Solution:
    import numpy as np
    def maximumSum(self, nums: List[int]) -> int:
        ans=-1
        d={}
        for i in  nums:
            
            
            k=i
            j = 0
            while k> 0:
                j+= k % 10  
                k //= 10
            if j in d :
                ans=max(ans,i+d[j])
            else:
                d[j]=i

            d[j]=max(d[j],i)
        
        return ans
            
                   



        
