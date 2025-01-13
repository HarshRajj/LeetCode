class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        cnt = 0
        for key in freq :
            if freq[key]%2 == 0 :
                cnt+= 2 
            else :
                cnt+=1 

        return cnt


        