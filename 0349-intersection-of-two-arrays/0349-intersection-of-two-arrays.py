class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        
        items = set()
        
        for item in nums1:
            items.add(item)
            
        for num in nums2:
            if num in items:
                res.append(num)
        
        return set(list(res))