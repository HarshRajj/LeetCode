class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxlen = 1
        n = len(s)
        if n == 1 :
            return s[0]
        if n==2 and s[0]==s[1] :
            return s

        for i in range(n) :

            l = i-1
            r = i+1
            while l>=0 and r < n and s[l] == s[r] :
                if r-l+1 > maxlen :
                    maxlen = r-l+1 
                    start = l 

                l -= 1 
                r += 1 

            l = i-1
            r = i 
            while l >= 0 and r < n and s[l] == s[r] :
                if r-l+1 > maxlen :
                    maxlen = r-l+1
                    start = l 

                l -= 1 
                r += 1 

        return s[start : start+maxlen] 
            






        