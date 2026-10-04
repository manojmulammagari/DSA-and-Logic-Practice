class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        left = 0
        right = len(height) - 1
        max_area = 0

        while (left < right):
            width = right - left
            
            if height[left] < height[right]:
                area = width * height[left]
                left += 1
            else:
                area = width * height[right]
                right -= 1
            if area > max_area:
                max_area = area

        return max_area