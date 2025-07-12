class Solution:
    def fn(self, ind, nums, ans , ds) : # backtracking

        if ind == len(nums):
            ans.append(ds[:]) 
            return 
        ds.append(nums[ind])
        self.fn(ind+1, nums, ans, ds) 
        ds.pop()
        self.fn(ind+1, nums, ans, ds)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        return self.bit_fn(nums)

        
    def bit_fn(self, nums): #bit manipulation
        n = len(nums)
        ans = []
        for num in range( 1<<n ) :
            ls = []
            for i in range(n):
                if (num  & (1<<i)) :
                    ls.append(nums[i])
            ans.append(ls) 

        return ans
        