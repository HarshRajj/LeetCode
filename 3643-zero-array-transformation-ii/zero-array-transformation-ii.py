class Solution:
    def minZeroArray(self, nums, queries):
        if not self.willBeZero(nums, queries, len(queries)):
            return -1
        
        lo, hi = 0, len(queries)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.willBeZero(nums, queries, mid):
                hi = mid
            else:
                lo = mid + 1
        
        return hi
    
    def willBeZero(self, arr, queries, k):
        d = [0] * (len(arr) + 1)
        
        for i in range(k):
            l, r, val = queries[i]
            d[l] += val
            if r + 1 < len(d):
                d[r + 1] -= val
        
        sum_ = 0
        for i in range(len(arr)):
            sum_ += d[i]
            if arr[i] > sum_:
                return False
        
        return True
