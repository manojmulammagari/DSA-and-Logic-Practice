class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the character and its most recent index position
        
        left = 0

        maxlength = 0

        for right, char in enumerate(s):

            # If the character is in the map AND its index is inside our current window
            if char in char_map and char_map[char] >= left:

                # Instantly jump the left pointer right past the old occurrence
                left = char_map[char] + 1

            # Update or insert the character's newest index position
            char_map[char] = right

            # Update the max length found so far
            maxlength = max(maxlength, right - left + 1)

        return maxlength
