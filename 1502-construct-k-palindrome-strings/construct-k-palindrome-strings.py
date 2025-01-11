class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        n = len(s)
        if k>n:
            return False
        cnt = 0
        dic =Counter(s) 
        for j in dic.keys():
            if dic[j]%2 != 0 :
                cnt +=1 



        if cnt>k :
            return False 
        
        return True

        
