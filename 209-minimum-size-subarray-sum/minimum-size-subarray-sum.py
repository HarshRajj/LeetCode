class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0 
        mini = float('inf')
        summ = 0
        for end in range(len(nums)) :
            if nums[end] >= target :
                return 1 

            summ+= nums[end]

            while summ >= target :
                mini = min(mini, end-start+1) 
                summ -= nums[start]
                start+=1  
            
        return mini if mini != float('inf') else 0 


            




        