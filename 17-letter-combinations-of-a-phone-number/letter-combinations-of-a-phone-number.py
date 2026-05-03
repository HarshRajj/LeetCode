class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': 'abc',
            '3': 'def', 
            '4':'ghi', 
            '5': 'jkl', 
            '6':'mno', 
            '7':'pqrs', 
            '8':'tuv', 
            '9':'wxyz'
        }
        def backtrack (idx, comb) :
            if idx == len(digits) :
                res.append(comb[:])
                return
            for letter in dic[digits[idx]] :
                backtrack(idx+1, comb+letter) 

        res=[]
        backtrack(0, "")

        return res

        

        