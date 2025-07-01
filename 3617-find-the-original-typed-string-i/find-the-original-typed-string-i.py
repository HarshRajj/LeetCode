class Solution:
    def possibleStringCount(self, s: str) -> int:
        ans = 1
        for i in range(len(s)-1) :
            if s[i] == s[i+1] :
                ans+=1
            else:
                continue 

        return ans

        