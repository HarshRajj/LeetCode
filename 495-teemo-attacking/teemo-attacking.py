class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        ans = 0
        n = len(timeSeries)
        for i in range(1, n) :
            if timeSeries[i]-timeSeries[i-1]  <= duration:
                ans += (timeSeries[i]-timeSeries[i-1])

            else :
                ans += duration 
        return ans+duration
                
            

        