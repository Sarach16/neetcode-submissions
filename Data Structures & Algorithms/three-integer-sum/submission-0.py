class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        nums.sort()
        result = list()
        if nums[0] > 0:
            return result 
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) -1
            while j < k :
                target = -nums[i]
                nums_sum = nums[j] + nums[k]
                if nums_sum == target:
                    triplet = [nums[i], nums[j], nums[k]]
                    result.append(triplet)
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j<k and nums[k] == nums[k+1]:
                        k -=1
                elif nums_sum < target:
                    j += 1
                elif nums_sum > target:
                    k -= 1

        return result
        