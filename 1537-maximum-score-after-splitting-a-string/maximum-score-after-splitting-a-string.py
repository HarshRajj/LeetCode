class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s) 
        ones= 0
        for i in s:
            if i == '1':
                ones+=1
        
        score = 0
        zeroes = 0 
        
        for i in range(0,n-1):
            if s[i] == '0':
                zeroes+=1
            else :
                ones-=1 
            
            score = max(score, zeroes + ones)

        return score





        