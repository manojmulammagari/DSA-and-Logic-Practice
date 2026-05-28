class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        b = []

        for i,n in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1

            while l<r:
                v=n+nums[l]+nums[r]
                if v>0:
                    r-=1
                elif v<0:
                    l+=1
                
                else :
                    b.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1

        return b