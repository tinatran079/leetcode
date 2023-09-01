class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # get the last index of nums1 - length
        last = m + n -1
        
        # merge in rev order, while there are elements in both arrays
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                # go to last pos and replace
                nums1[last] = nums1[m - 1]
                #update ptrs
                m -= 1
            else:
                nums1[last] = nums2[n -1]
                n -= 1
            last -= 1
        # edge case - if nums2 is not empty - fill nums1 w leftover nums2
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last -1
        
        
        
        