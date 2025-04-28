class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split() 
        i = 0 
        j = len(t)-1 
        while i<j :
            if t[i] == "":
                i+=1 
            if t[j] == "" :
                j-=1 

            t[i], t[j] = t[j], t[i] 
            i += 1
            j -= 1

        return " ".join(t)

        

        