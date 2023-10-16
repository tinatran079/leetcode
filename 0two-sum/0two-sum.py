class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        res = []
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in prev:
                res.append(prev[complement])
                res.append(index)
                return res
            prev[num] = index
        