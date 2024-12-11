class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        s = ""
        m = ""
        n = len(number)
        for i in range(n):
            if number[i]== digit :
                s = number[0:i]+number[i+1:]
            m = max(s,m)

        return m

            

        