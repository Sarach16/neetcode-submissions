class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        prefix = [1] * length
        postfix = [1] * length

        for i in range(1,length):
            prefix[i] = nums[i-1] * prefix[i-1]
        for j in range(length-2,-1,-1):
            postfix[j] = nums[j+1] * postfix[j+1]


        for k in range(length):
            output[k] = prefix[k] * postfix[k]
        return output




 




        