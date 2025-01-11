class Solution:
    def fn(self, res, arr,nums, map): 
        if len(arr)== len(nums): 
            res.append(arr[:])
            return 
            
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1] and map[i-1]==0 :
                continue
            if map[i] == 0 :
                map[i] = 1 
                arr.append(nums[i])
                self.fn(res, arr, nums, map) 
                arr.pop()
                map[i] = 0 
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 :
            return [nums]
        nums.sort() 
        res = []
        map = [0]*len(nums) 
        self.fn(res, [], nums, map) 
        return res
        