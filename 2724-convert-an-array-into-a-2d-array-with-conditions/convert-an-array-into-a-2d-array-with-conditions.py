class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = Counter(nums)
        ans = [] 
        while dic :
            tmp=[]
            for key in list(dic.keys()) :
                if dic[key]>0 :
                    tmp.append(key)
                    dic[key]-=1
                if dic[key]==0 :
                    dic.pop(key)
                
            ans.append(tmp)
            

            
            
        return ans


        