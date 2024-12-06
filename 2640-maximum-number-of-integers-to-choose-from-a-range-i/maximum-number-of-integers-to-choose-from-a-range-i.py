class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cnt = 0 
        summ = 0
        banned = set(banned)
        for i in range(1,n+1):
            if i in banned :
                continue 
            else :
                summ += i 
                if summ <= maxSum :
                    cnt += 1
                else :
                    break

        return cnt
        
        
                    


        

        


        