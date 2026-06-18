class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       return len(set(nums)) < len(nums)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       ## This solution is o(1) for space but o(nlogn) for time complexity
       ## because it used the sort function and loops through n elements once       
        # if not nums:
        #     return False 
        # nums.sort()
        # dummy = nums[0]
        # i = 1 
        # while i < len(nums):
        #     if dummy == nums[i]:
        #         return True
        #     else:
        #         dummy = nums[i]
        #         i += 1
        # return False 