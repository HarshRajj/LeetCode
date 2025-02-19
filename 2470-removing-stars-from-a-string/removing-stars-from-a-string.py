class Solution:
    def removeStars(self, s: str) -> str:
        stk = [] 
        for i in range(len(s)) :
            if s[i]== '*' :
                stk.pop()
            else:
                stk.append(s[i]) 

        return ''.join(stk)
            
        