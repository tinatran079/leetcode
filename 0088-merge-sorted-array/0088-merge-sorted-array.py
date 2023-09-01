class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers for nums1 and nums2
        i = m - 1  # Pointer for nums1
        j = n - 1  # Pointer for nums2
        last = m + n - 1  # Last index of the merged array nums1
        
        # Merge in reverse order while there are elements in both arrays
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
        
        # Edge case - if nums2 is not empty, fill nums1 with leftover nums2
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1
        
        
        
        