class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_len = len(numbers)
        result = list()
        # for i in range(num_len):
        #     for j in range(i+1, num_len):
        #         if numbers[i] + numbers[j] == target:
        #             result.extend([i+1, j+1])
        #             return result
        l = 0
        r = num_len - 1
        while l < r :
            sum = numbers[l] + numbers[r]
            if sum == target:
                result.extend([l+1,r+1])
                return result
            if sum < target:
                l += 1
            if sum > target:
                r -= 1


                
