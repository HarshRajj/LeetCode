class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        b = []
        i = 0
        j = 0 
        n = len(nums)
        m = 0 
        cnt = 0

        while True :
            if i < n :
                x = nums[i]
                if j<m and b[j] < x :
                    x = b[j]
                    j+=1
                else:
                    i+=1
            else:
                x = b[j]
                j+=1

            if x>=k :
                return cnt 
            if i < n :
                y = nums[i]
                if j<m and b[j] < y :
                    y = b[j]
                    j+=1
                else:
                    i+=1
            else:
                y = b[j]
                j+=1

            b.append( x*2 + y)
            m+=1 
            cnt+=1 

        return cnt


        




                






        '''
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
        '''



        
        