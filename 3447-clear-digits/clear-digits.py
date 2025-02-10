class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []

        for i in range(len(s)):
            if s[i].isdigit() :
                ans.pop()
            else:
                ans.append(s[i])

        return "".join(ans)
        
                
            
        