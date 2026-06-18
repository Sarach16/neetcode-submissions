class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums ={}
        for i,num in enumerate(nums):
            diff= target-num
            if diff in dict_nums:
                return [dict_nums[diff],i]
            else:
                dict_nums[num]=i

        


        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        #hashmap solution
        # dict_nums={}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in dict_nums:
        #         return [nums.index(diff),i]
        #     else:
        #         dict_nums[nums[i]]=i
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Brute force solution
        #have a loop that add up i and i+1 
        # i =0
        # j=1
        # while i < len(nums):
        #     while j <len(nums):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        #         else:
        #             j+=1
        #     i+=1
        #     j =i+1
        #if target is found return i and i+1 indices