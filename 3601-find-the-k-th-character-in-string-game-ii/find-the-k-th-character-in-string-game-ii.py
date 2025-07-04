class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        length = 1
        if k == 1 :
            return "a" 
        for i in operations :
            length *= 2 
            if length >= k :
                op = i
                newk = k - (length/2) 
                break 

        ch = self.kthCharacter(newk , operations)

        if op == 0 :
            return ch
        else:
            if ch == "z" :
                return "a"
            else: 
                return chr ( ord(ch) + 1 )

                
        