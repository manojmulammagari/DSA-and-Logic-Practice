class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            
            # 1. Eliminate min() by calculating area inside the pointer check

            if height[left] < height[right]:
                area = width * height[left]
                left += 1
            else:
                area = width * height[right]
                right -= 1
            
            # 2. Eliminate max() overhead using a pure comparison
            
            if area > maxi:
                maxi = area
                
        return maxi