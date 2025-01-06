class Solution:
    def fn(self, ind, nums, ans , ds) :

        if ind == len(nums):
            ans.append(ds[:]) 
            return 
        ds.append(nums[ind])
        self.fn(ind+1, nums, ans, ds) 
        ds.pop()
        self.fn(ind+1, nums, ans, ds)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        self.fn(0, nums, ans, ds) 
        return ans

        