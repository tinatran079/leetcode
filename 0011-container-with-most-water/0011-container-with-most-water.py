class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
#         Brute force
#         res = 0
        
#         for l in range(len(height)):
#             for r in range(l+1, len(height)):
#                 area = (r-l) * min(height[l], height[r])
#                 res = max(area, res)
                
#         return res
        
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(area, res)
            
            # update left and right ptrs, want to max heights
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res
            