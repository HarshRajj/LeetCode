class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        total = sum(candies)
        if total < k :
            return 0 

        l, r = 1, total // k 
        while l <= r :
            mid = (l + r) //2 
            count = 0 
            for c in candies :
                if c >= mid :
                    count += c // mid
                if count >= k :
                    break 

            if count >= k :
                res = mid 
                l = mid + 1 
            else: 
                r = mid -1 

        return res


        






        