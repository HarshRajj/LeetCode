class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        m = len(part)
        i=0 
        while i<n :
            if s[i:i+m] == part :
                s = s[:i] + s[i+m :] 
                if i-m > 0 :
                    i = i-m 
                else :
                    i = 0
                n-=m

            else :
                i+=1

        return s




