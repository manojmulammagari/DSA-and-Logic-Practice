class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        a = Counter(nums)

        if len(a)!= len(nums):
            return True

        else:
            return False