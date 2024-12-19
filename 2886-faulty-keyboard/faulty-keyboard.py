class Solution:
    def finalString(self, s: str) -> str:
        t = ""
        for i in range(len(s)) :
            if s[i]=='i' :
                t = t[::-1]
            else :
                t+= s[i]
        return t            
        