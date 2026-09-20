class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:

            return False
            
        original = x
        rev = 0
        
        # Pop the last digit off 'x' and push it onto the back of 'rev'
        while x > 0:
                
            digit = x % 10
            rev = (rev * 10) + digit
            x = x // 10
        
        # Compare the mathematically reversed number to the original
        return original == rev