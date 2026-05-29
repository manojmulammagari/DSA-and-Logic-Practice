class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxi=0

        left=0
        right =len(height)-1

        while left<right:
            n=right-left
            m=min(height[right],height[left])
            maxi=max(n*m,maxi)

            if height[left]<height[right]:
                left+=1
            elif height[left]>height[right]:
                right-=1

            else:
                right-=1
            

        return maxi

            


