class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        
        i = 0 
        ans = 0 
        while k>0 and happiness[i]-i > 0 :
            ans += happiness[i]- i 
            i += 1
            k -= 1
        return ans