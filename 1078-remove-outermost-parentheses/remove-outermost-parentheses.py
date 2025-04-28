class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        bal = 0 
        res = ""
        for i in s :
            if i == '(' :
                if bal > 0 :
                    res += i 
                bal += 1 

            else :
                bal -= 1

                if bal > 0 :
                    res += i 


        return res                

        