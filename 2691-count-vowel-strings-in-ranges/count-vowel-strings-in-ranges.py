class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = [] 
        vow = "aeiou"
        left = [0]*len(words)
        p = words[0] 
        if p[0] in vow and p[len(p)-1] in vow :
            left[0] = 1 

        for i in range(1,len(words)):
            x = words[i]
            if x[0] in vow and x[len(x)-1] in vow :
                left[i] = left[i-1]+1 

            else :
                left[i] = left[i-1]

        for i in queries :
            if i[0] == 0 :
                ans.append(left[i[1]]) 
            else :
                ans.append(left[i[1]]-left[i[0]-1])   

        return ans    