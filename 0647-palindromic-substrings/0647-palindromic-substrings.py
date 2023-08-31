class Solution(object):
    def expand(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    def countSubstrings(self, s):
        total_count = 0
        
        for center in range(len(s)):
            total_count += self.expand(s, center, center)
            total_count += self.expand(s, center, center + 1)
            
        return total_count

