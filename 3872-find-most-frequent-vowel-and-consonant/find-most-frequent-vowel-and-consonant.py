class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = Counter(s)
        max_c, max_v = 0, 0
        vow = "aeiou"
        for k, val in freq.items():
            if k in vow :
                max_v = max(max_v,val )

            else:
                max_c = max(max_c, val )

        return max_c + max_v 