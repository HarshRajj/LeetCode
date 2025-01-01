class Solution:
    def fn (self, ind, arr, ans, target, ds):
        if ind == len(arr) : 
            if target == 0 :
                ans.append(ds[:]) 
            return 

        if arr[ind]<=target :
            ds.append(arr[ind])
            self.fn (ind, arr, ans, target-arr[ind], ds)
            ds.pop()


        self.fn (ind+1, arr, ans, target, ds) 



    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds=[]
        self.fn(0, candidates,ans, target, ds) 

        return ans

        