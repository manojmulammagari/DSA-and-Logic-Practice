class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        left =0
        right = len(height) -1
        max_area = 0

        while left < right:
            width = right - left

            if height[left]<height[right]:
                a = height[left]*width
                max_area=max(max_area,a)
                left +=1

            else:

                b = height[right]*width
                max_area=max(max_area,b)
                right-=1
        return max_area



