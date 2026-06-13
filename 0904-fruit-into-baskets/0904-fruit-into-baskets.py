class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l = 0
        m = 0
        window = {}

        have = 0

        for r in range(len(fruits)):

            c = fruits[r]
            # Add the current fruit to our window frequency map
            window[c] = 1 + window.get(c, 0)

            # If we have more than 2 types of fruit, shrink the window from the left
            while len(window) > 2:
                left_fruit = fruits[l]
                window[left_fruit] -= 1

                # CRITICAL: If the fruit count drops to 0, completely remove the key
                if window[left_fruit] == 0:
                    del window[left_fruit]

                # Move the left pointer forward
                l += 1

            # Update the maximum length of a valid window
            v = r - l + 1
            m = max(m, v)

        return m
