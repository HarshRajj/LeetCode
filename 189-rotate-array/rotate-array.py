class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        ans= [0]*n
        for i in range (n):
            ans[(i+k)%n] = nums[i] 
        
        for i in range(n):
            nums[i] = ans[i]
     
        

        