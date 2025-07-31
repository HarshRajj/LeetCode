class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = Counter(s)
        tc = Counter(t)

        ans = 0 

        for key, val in tc.items():
            if key in sc:
                if val > sc[key]:
                    ans += val - sc[key]
            else:
                ans += val

        return ans


        


        