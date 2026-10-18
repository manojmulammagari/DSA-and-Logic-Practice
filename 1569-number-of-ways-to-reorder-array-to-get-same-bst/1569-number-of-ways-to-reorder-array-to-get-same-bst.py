import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # math.comb computes combinations: C(len(left) + len(right), len(left))
            ways_comb = math.comb(len(left) + len(right), len(left)) % MOD
            
            ways_left = dfs(left)
            ways_right = dfs(right)
            
            return (ways_comb * ways_left * ways_right) % MOD

        # Subtract 1 because the problem asks for *re-orderings* (excluding the original array itself)
        return (dfs(nums) - 1 + MOD) % MOD