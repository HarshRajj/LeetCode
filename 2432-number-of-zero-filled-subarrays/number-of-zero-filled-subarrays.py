class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        ans = 0 
        c = 0
        for n in nums :
            if n == 0 :
                c += 1
                ans += c 
            else :
                c = 0 

        return ans
        