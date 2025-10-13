class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def is_anagram(s1, s2):
            return sorted(s1)==sorted(s2)

        ans = [] 
        for word in words :
            if ans and is_anagram(ans[-1], word):
                continue 
            ans.append(word)

        return ans

            

            

        