class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort() 
        n = len(events)
        pq = [] 
        day = events[0][0]
        i = 0 
        cnt = 0 
        
        while pq or i< n :

            if not pq :
                day = events[i][0]
            while i<n and events[i][0] == day :
                heapq.heappush( pq, events[i][1]) 
                i+=1

            if pq :
                heapq.heappop (pq)
                cnt += 1

            day += 1

            while pq and pq[0] < day :
                heapq.heappop(pq)

        return cnt
        

        