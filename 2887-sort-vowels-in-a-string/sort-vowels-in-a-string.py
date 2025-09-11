class Solution:
    def sortVowels(self, s: str) -> str:
        vow = []
        lis = list(s)

        for i in lis :
            if i in "AEIOUaeiou" :
                vow.append(i)
        if vow  == []:
            return s 
        vow.sort()
        count = 0 

        for j in range(len(s)):
            if lis[j] in "AEIOUaeiou":
                lis[j] = vow[count] 
                count += 1 
        return "".join(lis)