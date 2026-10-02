class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Calculate prefix products and store them in 'answer'
        prefix = 1
        for i in range(n):
            answer[i] = prefix          # Store the product of all elements to the left
            prefix *= nums[i]           # Update the running prefix product
            
        # Step 2: Calculate suffix products on the fly and multiply with the prefix
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix         # Multiply the existing prefix product by the suffix product
            suffix *= nums[i]           # Update the running suffix product
            
        return answer