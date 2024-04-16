class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # return an array of their intersection
        
        my_dict= {}
        res = []
        
        for num in nums1:
            my_dict[num] = True 
            
        for n in nums2:
            if n in my_dict:
                res.append(n)
        return list(set(res))
                