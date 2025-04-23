import math
class Solution:
    def totalHours (self, piles : List[int], rate:int) -> int :
        total = 0
        n = len(piles)
        for i in range(n):
            total += math.ceil (piles[i] / rate ) 
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int: 

        low= 1
        high = max(piles) 
        
        while low <= high : 
            mid = low + (high-low)//2 

            totalHours = self.totalHours(piles, mid)

            if totalHours <= h :
                high = mid-1
            else :
                low = mid+1 

        return low
            
        