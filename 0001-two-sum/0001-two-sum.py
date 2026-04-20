class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a = {}

        for i ,n in enumerate(nums):

            complement= target-n

        
            if complement in a:
                return[a[complement],i]

            a[n]=i

    











