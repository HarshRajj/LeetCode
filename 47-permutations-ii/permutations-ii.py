class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(ind):
            if ind == len(nums):
                res.append(nums[:])
                return
            
            used = set()
            for i in range(ind, len(nums)):
                if nums[i] in used: 
                    continue
                used.add(nums[i])
                nums[ind], nums[i] = nums[i], nums[ind]
                backtrack(ind + 1)
                nums[ind], nums[i] = nums[i], nums[ind] 

        res = [] 
        nums.sort() 
        backtrack(0) 
        return res