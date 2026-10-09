class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

        # seen = set()

        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)

        # return False
