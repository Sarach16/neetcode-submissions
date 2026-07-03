class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        for i in range(1,len(height)-1):
            max_l = max(height[:i])
            max_r = max(height[i+1:])
            capacity = min(max_l, max_r) - height[i]
            if capacity > 0:
                total_water += capacity
        return total_water

