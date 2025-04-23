class Solution:
    def possible(self, arr, day, m, k):
        c = 0 
        bo = 0
        for i in range(len(arr)) : 
            if arr[i] <= day :
                c += 1 
            else:
                bo += (c//k )
                c = 0 

        bo += (c//k )
        
        return bo >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k :
            return -1 
        low = min(bloomDay) 
        high = max(bloomDay) 

        while ( low <= high ) :
            mid = low+(high-low)//2 
            if self.possible(bloomDay, mid, m, k) :
                high = mid - 1 
            else:
                low = mid + 1

        return low 

        

    