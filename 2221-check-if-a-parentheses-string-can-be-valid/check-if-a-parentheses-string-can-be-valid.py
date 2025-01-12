class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        if n%2 != 0:
            return False
        
        op = 0 
        for i in range(n):
            if s[i] == '(' or locked[i] == '0' :
                op += 1 
            else :
                op -= 1 
            if op < 0 :
                return False #more ')' found than possible conversions 

        cl = 0 
        for j in range(n-1,-1,-1):
            if s[j] == ')' or locked[j] == '0' :
                cl += 1 
            else:
                cl -= 1 
            if cl < 0 :
                return False 

        return True 



        






        
        
        