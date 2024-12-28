class Solution:
    def recur(self, ind , nums , ans) :
        if ind == len(nums):
            ans.append(nums[:])
            return
        for i in range(ind, len(nums)):
            nums[i], nums[ind] = nums[ind], nums[i]
            self.recur(ind+1, nums, ans)
            nums[i], nums[ind] = nums[ind], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.recur(0,nums, ans) 
        return ans
        