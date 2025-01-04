class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for ch in range(26):
            c = chr(ord('a') + ch)
            leftIdx, rightIdx = s.find(c), s.rfind(c)
            if leftIdx != rightIdx:
                res += len(set(s[leftIdx+1:rightIdx]))

        return res
        