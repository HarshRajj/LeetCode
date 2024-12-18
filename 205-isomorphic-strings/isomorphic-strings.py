class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t) :
            return false 
        p = {} 
        q = {}
        for i in range(len(s)):

            if s[i] in p and p[s[i]] != t[i]:
                return False 
            if t[i] in q and q[t[i]] != s[i]:
                return False
            p[s[i]] = t[i] 
            q[t[i]] = s[i]
            

        return True
            


        
        
        


        