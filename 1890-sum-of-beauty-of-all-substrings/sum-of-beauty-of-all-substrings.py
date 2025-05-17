class Solution:
    
    def getMin(self, arr) -> int : # to exclude 0 as minimum frequency,
        mini = float('inf')
        for i in arr :
            if i != 0 : 
                mini = min(mini, i) 
        return mini

    def beautySum(self, s: str) -> int:
        n = len(s) 
        if n<3 :
            return 0

        
        total = 0
        for i in range(n) :
            freq = [0]*26
            for j in range(i, n) :
                freq[ord(s[j])-ord('a')] += 1 

                beauty = max(freq)- self.getMin(freq) 
                total += beauty

        return total
