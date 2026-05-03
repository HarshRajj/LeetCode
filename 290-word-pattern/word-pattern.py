class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:\

        words = s.split()
        if len(pattern) != len(words) :
            return False

        char_word = {}
        word_char = {} 

        for char, word in zip(pattern, words) :
            if char in char_word :
                if char_word[char]!= word :
                    return False
            else :
                char_word[char] = word
            if word in word_char :
                if word_char[word]!= char :
                    return False
            else :
                word_char[word] = char 

        return True
            


        

        