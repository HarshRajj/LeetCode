class Solution:
    def smallestPalindrome(self, s: str) -> str:

        n = len(s)
        if n<=1 :
            return s 
        t = ''.join(sorted(s[:n//2]))
        if n%2 == 1 :
            m = n//2
            return t + s[m] + t[::-1]
        else :
            return t + t[::-1]

        

        

        

        