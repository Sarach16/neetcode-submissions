class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #amount of water = min height * distance(width)
        i = 0 
        j = len(heights) - 1
        max_water = (j - i) * min(heights[i], heights[j])
        while i < j :
            amount_w = (j - i) * min(heights[i], heights[j])
            if amount_w > max_water:
                max_water = amount_w
        
            if heights[i] < heights[j]:
                i+= 1
            else: j -= 1
        
        return max_water
            
