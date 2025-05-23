class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = len(s)
        for key, val in freq.items() :
            while val>=3:
                val-=2
                ans-=2
 

        return ans


        