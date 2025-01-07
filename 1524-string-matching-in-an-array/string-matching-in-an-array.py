class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        n = len(words)
        for i in range(n):
            k=0
            for j in range(n) :
                if i!=j:
                    if words[i] in words[j] :
                        k=1
                         
            if k :
                ans.append(words[i])


        return ans
                
        
        
        