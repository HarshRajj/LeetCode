class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        subSum = sum(nums[:k])
        maxSum = subSum

        l = 1 
        r = k

        while (r<len(nums)):
            subSum += nums[r]- nums[l-1]
            maxSum = max(maxSum,subSum)
            r+=1 
            l+=1 
        return maxSum/k


        

        


        