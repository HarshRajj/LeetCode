class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        n = len(startTime)
        
        gaps = [startTime[0]] +[startTime[i]- endTime[i-1] for i in range(1, n)] + [eventTime-endTime[-1]]
        sz = min(k+1, n+1)
        curr = sum ( gaps[:sz] )
        maxi = curr

        for i in range(sz, len(gaps)) :
            curr += gaps[i]- gaps[i-sz]
            if curr> maxi :
                maxi = curr 

        return maxi

        


        


        