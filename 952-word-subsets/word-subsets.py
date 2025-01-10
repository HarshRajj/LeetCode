class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        k =  False
        dic2=Counter()

        
        for word in words2:
            c = Counter(word)
            for char in c:
                dic2[char] = max(dic2[char], c[char])
        
        for word in words1 :
            dic = Counter(word) 
            
            for j in dic2.keys() :
                if j in dic and dic2[j]<=dic[j] :
                    
                    k = True
                else :
                    k = False 
                    break
                    
            if k :
                ans.append(word) 

        return ans


            
                

        




        