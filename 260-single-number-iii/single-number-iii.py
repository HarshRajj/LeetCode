class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = Counter(nums) 
        ans = []
        for key in dic.keys():
            if dic[key]==1:
                ans.append(key)
            else:
                continue
                
        return ans



        
        