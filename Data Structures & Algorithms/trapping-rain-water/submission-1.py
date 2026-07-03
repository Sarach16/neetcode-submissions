class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = list()
        suffix_max = list()
        total_water = 0

        max_left = 0
        for h in height:
            max_left = max(max_left, h)
            prefix_max.append(max_left)
        
        max_right = 0
        for i in range(len(height) -1, -1 , -1):
            max_right = max(max_right, height[i])
            suffix_max.append(max_right)
        
        for j in range(len(height)):
            water_amount = min(prefix_max[j], suffix_max[len(height)-1-j]) - height[j]
            if water_amount > 0:
                total_water += water_amount
        return total_water




        # total_water = 0
        # for i in range(1,len(height)-1):
        #     max_l = max(height[:i])
        #     max_r = max(height[i+1:])
        #     capacity = min(max_l, max_r) - height[i]
        #     if capacity > 0:
        #         total_water += capacity
        # return total_water

