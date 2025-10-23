class Solution:
    def hasSameDigits(self, s: str) -> bool:
        i = 0 
        ans = ""
        while len(s)>2 and i < len(s)-1:
            ans += str((int(s[i]) + int(s[i+1])) % 10) 
            i+= 1
            if i == len(s)-1 :
                s = ans 
                i = 0 
                ans = ""
        return len(s) == 2 and s[0] == s[1]

        