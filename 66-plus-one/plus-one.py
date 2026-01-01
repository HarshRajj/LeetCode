class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        k = 0
        for i in digits :
            k = k*10 + i 

        k += 1
        while k!=0 :
            ans.append(k%10)
            k //= 10
        return list(reversed(ans))
            