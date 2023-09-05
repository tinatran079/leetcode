class Solution(object):
    def longestWord(self, words):
        words.sort()
        
        built_words = set()
        longest_word = ""
        
        for word in words:
            if len(word) == 1 or word[:-1] in built_words:
                built_words.add(word)
            
                # for last word if it's longest
                if len(word) > len(longest_word):
                    longest_word = word
                
        return longest_word
                    