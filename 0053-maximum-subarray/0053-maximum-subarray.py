class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=cur=nums[0]

        for n in nums[1:]:
            cur=max(n,cur+n)
            maxs=max(cur,maxs)

        return maxs