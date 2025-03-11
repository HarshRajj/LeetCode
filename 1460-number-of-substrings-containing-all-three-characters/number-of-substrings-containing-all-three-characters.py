class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0 
        i = 0 
        dic = {'a' : 0 , 'b' : 0 , 'c' : 0 }

        for j in range(len(s)):
            dic [s[j]] += 1 

            while dic['a']> 0 and dic['b']> 0 and dic['c']> 0 :
                count += len(s)-j
                dic [s[i]] -= 1
                i+=1 

        return count

 

