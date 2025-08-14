class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        ones = 0
        zeros = 0
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] == "0":
                zeros += 1
            else:
                ones += 1

            while ones > k and zeros > k:
                if s[l] == "0":
                    zeros -= 1
                else:
                    ones -= 1
                l += 1

            res += (r - l + 1)
        return res
                



        