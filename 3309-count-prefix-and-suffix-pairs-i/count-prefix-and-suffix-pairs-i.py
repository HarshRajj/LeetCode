class Solution:
    def isPrefixAndSuffix(self, str1, str2):

        if len(str1)>len(str2):
            return False
        else :
            return str2.startswith(str1) and str2.endswith(str1) 
        

    def countPrefixSuffixPairs(self, words: List[str]) -> int: 
        n = len(words)
        count = 0
        for i in range(n-1):
            for j in range(i+1, n) :
                if self.isPrefixAndSuffix(words[i], words[j]) :
                    count+=1 

        return count
        