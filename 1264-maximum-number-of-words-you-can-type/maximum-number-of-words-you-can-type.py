class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        return sum(1 for w in text.split() if not any (c in brokenLetters for c in w))

        '''
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
        '''
        
                
        