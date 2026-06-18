class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    ## iterate over nums and have a dummy var that holds the first value compares it to the seond
    ## update dummy variable every time there is a new value, remove the duplicates as you go
        dummy= nums[0]
        i = 1
        while i < len(nums):
            if dummy == nums[i]:
                del nums[i]
            else:
                dummy = nums[i]
                i += 1
        return len(nums)

   