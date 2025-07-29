class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        
        # ans = [] 
        # for i in nums :
        #     if i%2 == 0 :
        #         ans.append(0)
        #     else: 
        #         ans.append(1) 
        # return sorted(ans)
        
        return sorted([i%2 for i in nums])
        
        