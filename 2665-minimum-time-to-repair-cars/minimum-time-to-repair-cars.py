import math

class Solution:
    def solve(self, res, ranks, cars):
        cnt = 0
        for rank in ranks:
            cnt += int(math.sqrt(res / rank))
        return cnt >= cars

    def repairCars(self, ranks, cars):
        low, high = 1, max(ranks) * cars * cars
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if self.solve(mid, ranks, cars):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans