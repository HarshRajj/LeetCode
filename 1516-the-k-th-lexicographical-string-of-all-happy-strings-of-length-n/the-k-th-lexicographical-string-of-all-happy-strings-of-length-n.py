class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        sz = 3*(1<<(n-1))
        if k>sz: return ""

        q, r=divmod(k-1, 1<<(n-1))
        s=[' ']*n
        s[0]=chr(ord('a') + q)

        xx = [['b', 'c'], ['a', 'c'], ['a', 'b']]
        
        for i in range(n-1):  # Iterating from 0 to n-2
            idx=ord(s[i]) - ord('a')
            s[i+1]=xx[idx][1] if r&(1<<(n-i-2)) else xx[idx][0]

        return "".join(s) 