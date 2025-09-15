class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        res = 0 
        k = 0 
        while k< len(text): 
            if text[k] in brokenLetters:
                while k < len(text) and text[k] != " " :
                    k += 1 
            elif text[k] == " " or k == len(text)- 1 :
                res += 1
            k+= 1
        return res
        
                
        