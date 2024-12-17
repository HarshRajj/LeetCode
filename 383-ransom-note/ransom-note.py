class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for x in magazine :
            d[x] = d.get(x,0) + 1 

        for y in ransomNote :
            if y not in d or d[y]<=0 :
                return False 
            else :
                d[y] -= 1
        return True