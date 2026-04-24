class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r = 0
        l = 0
        u = 0
        for i in moves :
            if i == 'R': 
                r += 1
            elif i =='L' :
                l+=1 
            else : 
                u+=1

        if l<r :
            r+=u
        else :
            l+=u 

        return abs(l-r)
        