class Solution(object):
    def longestWord(self, words):
        words.sort()
        
        built_words = set()
        longest = ""
        
        for word in words:
            if len(word) == 1 or word[:-1] in built_words:
                built_words.add(word)
                
                if len(word) > len(longest):
                    longest = word
                    
        return longest