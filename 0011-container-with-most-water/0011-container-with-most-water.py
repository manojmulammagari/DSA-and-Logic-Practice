class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate area once per loop
            current_height = min(height[left], height[right])
            max_area = max(max_area, current_height * (right - left))

            # Move the pointer of the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area