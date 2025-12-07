class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        most_water = 0

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            if water > most_water:
                most_water = water
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most_water
        
