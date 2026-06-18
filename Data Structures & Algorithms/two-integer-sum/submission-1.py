class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #have a loop that add up i and i+1 
        i =0
        j=1
        while i < len(nums):
            while j <len(nums):
                if nums[i]+nums[j] == target:
                    return [i,j]
                else:
                    j+=1
            i+=1
            j =i+1
        #if target is found return i and i+1 indices