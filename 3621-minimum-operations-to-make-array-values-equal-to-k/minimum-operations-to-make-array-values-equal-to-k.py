class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        dic = {} 
        for i in nums :
            if i < k :
                return -1 
            elif i > k :
                dic[i]  = dic.get(i,0) + 1 
        return len(dic)
        