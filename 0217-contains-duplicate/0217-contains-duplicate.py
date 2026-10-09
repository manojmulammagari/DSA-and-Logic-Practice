class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False
