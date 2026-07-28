class Solution:
    from collections import Counter
    def smallestPalindrome(self, s: str) -> str:

        n = len(s)
        freq = Counter(s[:n // 2])
        st = "abcdefghijklmnopqrstuvwxyz"
        h = ''.join([ch * freq[ch] for ch in st]) 
        mid = s[n // 2] if n % 2 != 0 else ""
        return h + mid + h[::-1]
        

        

        

        