class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a = {}

        for i,n in enumerate(nums):
            need = target - n

            if need in a:
                return[a[need],i]

            a[n] = i



