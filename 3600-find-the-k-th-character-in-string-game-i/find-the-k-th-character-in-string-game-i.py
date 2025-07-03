class Solution:
    def kthCharacter(self, k: int) -> str:
        initial = ["a"]
        while True :
            new = []
            for s in initial :
                if s!= "z":
                    new.append(chr(ord(s)+1)) 
                else :
                    new.append("a")
            initial = initial + new 
            if len(initial) >= k :
                return initial[k-1]

        return
        