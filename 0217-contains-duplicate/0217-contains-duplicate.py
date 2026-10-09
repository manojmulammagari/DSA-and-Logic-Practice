class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
      return True if len(set(nums)) != len(nums) else False