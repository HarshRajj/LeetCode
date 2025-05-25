class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        def rev(word:str) -> str :
            return word[::-1]

        mpp = {} 
        res = 0 

        for word in words :
            r = rev(word)
            if r in mpp  and mpp[ r ] > 0 :
                res += 4 
                mpp[r] -= 1
            else :
                mpp[word] = mpp.get(word, 0)+1

        for key, val in mpp.items() :
            if key[0] == key[1] and val > 0 :
                res += 2 
                break

        return res 
            

            
        