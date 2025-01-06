class Solution:
    def fn(self, ind, nums, ans , ds) :

        ans.append(ds[:])
        
        for i in range(ind,len(nums)):
            if i != ind and nums[i] == nums[i-1]:
                continue 

            ds.append(nums[i])
            self.fn(i+1, nums, ans, ds) 
            ds.pop() 


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        ds = [] 
        self.fn(0, nums, ans, ds) 
        return ans
        