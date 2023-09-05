class Solution(object):
    def longestWord(self, words):
        words.sort()

        # Create a set to store the words that can be built
        built_words = set()

        # Initialize the longest word found so far
        longest = ""

        for word in words:
            # If the word has only one character or the prefix of the word is in built_words
            if len(word) == 1 or word[:-1] in built_words:
                # Add the word to the built_words set
                built_words.add(word)

                # Update the longest word if needed
                if len(word) > len(longest):
                    longest = word

        return longest