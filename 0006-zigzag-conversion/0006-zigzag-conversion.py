class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is 1 or greater than or equal to the string length,
        # no zigzag pattern is formed; return the string as is.
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            # Reverse direction when we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            current_row += 1 if going_down else -1

        # Join all rows together to get the final converted string
        return ''.join(rows)