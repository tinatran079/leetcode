class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    # search right portion
                    l = mid + 1
                else:
                    # search left portion
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    # search left portion
                    r = mid - 1
                else:
                    # search right portion
                    l = mid + 1
                    
        return - 1
        