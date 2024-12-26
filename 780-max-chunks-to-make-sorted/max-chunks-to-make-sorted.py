class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        n = len(arr) 
        k = 0 
        maxi = 0
        count = 0
        while k < n :
            maxi = max(arr[:k+1])
            
              
            if maxi==k :
                count+=1
            k+=1
                
        return count
                
           

        
        
        
        
        