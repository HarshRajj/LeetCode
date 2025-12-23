class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        current_max = -1 
        max_value = [-1]*n
        ans = 0 
        events.sort()

        for i in range(n-1, 0, -1):
            current_max = max(current_max, events[i][2]) 
            max_value[i] = current_max 

        for i in range (n) :
            left = i+1 
            right = n-1 
            leftmost = -1
            while left <= right :
                mid = left+(right-left)//2 
                if events[mid][0] > events[i][1] :
                    leftmost = mid 
                    right = mid-1 

                else :
                    left = mid+1 
            if leftmost == -1 :
                ans = max(ans, events[i][2]) 
            else :
                ans= max ( ans, events[i][2] + max_value[leftmost])
        return ans
                
