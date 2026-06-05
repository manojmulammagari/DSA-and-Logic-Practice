class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        l,r,b=0,len(nums)-1,-1

        while l<=r:
            m=l+(r-l)//2

            if nums[m]==target:
                return m

            if nums[m]<=target:
                l= m+1

            else:
                r=m-1

        return b