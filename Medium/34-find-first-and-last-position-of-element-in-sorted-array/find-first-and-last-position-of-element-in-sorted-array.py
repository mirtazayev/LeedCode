class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [nums.index(target), len(nums) - 1 - nums[::-1].index(target)] if target in nums else [-1, -1]
