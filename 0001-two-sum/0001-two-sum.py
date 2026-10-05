class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a = {}

        for i,n in enumerate(nums):
            sub = target - n

            if sub in a:
                return[a[sub],i]

            a[n] = i



