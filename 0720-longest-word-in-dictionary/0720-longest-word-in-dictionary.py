class Solution(object):
    def longestWord(self, words):
        words.sort()
        
        set_words = set()
        longest = ""
        
        for word in words:
            if len(word) == 1 or word[:-1] in set_words:
                set_words.add(word)
                
                if len(word) > len(longest):
                    longest = word
                    
        return longest
    