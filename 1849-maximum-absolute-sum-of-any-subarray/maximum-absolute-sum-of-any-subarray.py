class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sum = 0
        for i in nums : 
            sum += i 
            if sum <0 :
                sum = 0 
            maxi = max(sum, maxi) 

        mini = float('inf') 
        sum = 0 
        for j in nums:
            sum+=j
            if sum>0 :
                sum = 0 
            mini = min(mini, sum )

        return max(maxi, abs(mini))
        