class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        ans, left, ones = 0, 0, 0 
        for right, n in enumerate(s) :
            ones += 1 if n == "1" else 0 
            while ones > k and right - left + 1 - ones > k :
                ones -= 1 if s[left] == "1" else 0 

                left += 1
            ans += right-left + 1

        return ans

                



        