class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []
        ans = 0
        for num in nums:
            heapq.heappush ( min_heap , num )

        
        while len(min_heap)>=2 : 
            x = heapq.heappop(min_heap)
            if x<k:
                y = heapq.heappop(min_heap)
                p = min(x,y)*2 + max(x,y)

                heapq.heappush(min_heap, p)
                ans+=1
            else:
                break

        return ans

        
        