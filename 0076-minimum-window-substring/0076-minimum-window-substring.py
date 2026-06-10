class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s is "" or t is "" or len(s) < len(t):
            return ""

        target_count = Counter(t)

        unique = len(target_count)

        window = {}

        left = 0

        formed_char = 0

        min_len = len(s) + 1

        bestleft = 0

        bestright = 0

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in target_count and window[char] == target_count[char]:

                formed_char = formed_char + 1

            while formed_char == unique:

                curlen = right - left + 1

                if curlen < min_len:

                    min_len = curlen
                    bestleft = left
                    bestright = right

                charl = s[left]

                window[charl] = window.get(charl, 0) - 1

                if charl in target_count and window[charl] < target_count[charl]:

                    formed_char = formed_char - 1

                left = left + 1

        if min_len == len(s) + 1:

            return ""

        else:
            
            return s[bestleft : bestright + 1]
