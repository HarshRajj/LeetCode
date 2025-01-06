class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int) 
        for i in nums :
            dic[i]+=1 

        for key in dic.keys():
            if dic[key]<3:
                return key

        