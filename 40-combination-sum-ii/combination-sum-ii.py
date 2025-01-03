class Solution:
    def fn (self, ind, arr, ans, target, ds):
        if target == 0 :
            ans.append(ds[:])
            return 
        
        for i in range (ind, len(arr)) :
            if i> ind and arr[i] == arr[i-1] :
                continue 

            if arr[i]> target :
                break 
            ds.append(arr[i])
            self.fn(i+1, arr, ans, target-arr[i], ds )
            ds.pop() 
             
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        ds = [] 
        self.fn(0, candidates, ans, target, ds )
        return ans

        