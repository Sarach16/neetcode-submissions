class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #convert array to set to reduce search time
        nums_set = set(nums)
        sequences = list()
        nums_len = len(nums_set)
        for num in nums_set:
            sequence = list()
            if (num - 1) not in nums_set:
                sequence.append(num)
                for j in range(1,nums_len):
                    if num + j in nums_set:
                        sequence.append(num + j)
                    else: break
                sequences.append(sequence)
        return max(map(len, sequences),default = 0)
        

        
            
            