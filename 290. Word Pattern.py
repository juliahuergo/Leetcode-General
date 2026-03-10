class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        patterns = {}
        letters = {}
        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            letter, word = pattern[i], words[i]
            if (letter in letters and letters[letter] != word) or (word in patterns and patterns[word] != letter): #already mapped letter to another word or word to another letter
                return False
            elif letter not in letters and word not in patterns:
                letters[letter] = word
                patterns[word] = letter
        
        return True
             
