class Solution:
    def count(self, nums, div) :
        summ = 0
        for num in nums :
            summ += math.ceil ( num/div )

        return summ


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        low = 1
        high = max(nums)

        while ( low <= high) :
            mid = low + (high-low)//2 

            if self.count(nums, mid ) <= threshold :
                high = mid - 1 
            else :
                low = mid + 1

        return low

        