class Solution(object):
    def isAnagram(self, s, t):
        return self.char_count(s) == self.char_count(t)

    def char_count(self, str):
        count = {}

        for char in str:
            if char not in count:
                count[char] = 0
            count[char] += 1
        
        return count