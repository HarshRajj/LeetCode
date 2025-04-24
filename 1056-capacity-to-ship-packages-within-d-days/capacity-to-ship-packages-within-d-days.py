class Solution:
    def noOfDays (self, wt, cap ):
        days = 1
        load = 0 
        for i in range(len(wt)):
            if load + wt[i] > cap :
                load = wt[i] 
                days += 1 
            else:
                load += wt[i] 
        return days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights) 
        high = sum(weights) 

        while (low <= high) :
            mid = ( low + high ) // 2
            if self.noOfDays ( weights, mid) <= days :
                high = mid-1 
            else:
                low = mid+1 

        return low
        