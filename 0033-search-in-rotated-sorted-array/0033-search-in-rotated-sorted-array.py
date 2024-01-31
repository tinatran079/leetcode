class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # left sorted portion is greater than right sorted
        # we know if the mid is >= left pointer, we are in the left sorted portion
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                # in left sorted portion
                if target > nums[mid] or target < nums[l]:
                    # search right side
                    l = mid + 1
                else:
                    r = mid -1
                    
            else:
                if target < nums[mid] or target > nums[r]:
                    # search left side
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1