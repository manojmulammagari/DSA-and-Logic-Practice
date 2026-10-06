class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a = {}

        for i,n in enumerate(nums):
            compliment  = target - n

            if compliment in a:
                return[a[compliment],i]

            a[n] = i