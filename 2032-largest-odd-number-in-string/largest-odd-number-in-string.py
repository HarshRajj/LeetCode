class Solution:
    def largestOddNumber(self, num: str) -> str:
        maxi = -1 
        if int(num[-1])%2 == 0:
            for i in range(len(num)-1, -1, -1) :
                if int(num[i])%2 == 0 :
                    continue 
                else :
                    return num[:i+1]

        else :
            return num  

        return ""   