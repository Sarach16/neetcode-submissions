class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False 
        nums.sort()
        dummy = nums[0]
        i = 1 
        while i < len(nums):
            if dummy == nums[i]:
                return True
            else:
                dummy = nums[i]
                i += 1
        return False 