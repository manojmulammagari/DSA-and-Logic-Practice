class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == "" or t == "" or len(s) < len(t):

            return ""

        t_count = Counter(t)

        window = {}

        unique = len(t_count)

        formed = 0

        left = 0

        bestleft = 0

        bestright = 0

        minimum = len(s) + 1

        for right in range(len(s)):
            ch = s[right]

            window[ch] = 1 + window.get(ch, 0)

            if ch in t_count and window[ch] == t_count[ch]:
                formed += 1

            while formed == unique:

                current_length = right - left + 1

                if current_length < minimum:
                    minimum = current_length
                    bestleft = left
                    bestright = right

                char_left = s[left]

                window[char_left] = window.get(char_left, 0) - 1

                if char_left in t_count and window[char_left] < t_count[char_left]:

                    formed -= 1

                left += 1

        if minimum == len(s) + 1:
            return ""

        else:
            return s[bestleft : bestright + 1]

        # if s == "" or t == "" or len(s) < len(t):
        #     return ""

        # counT, window = Counter(t), {}

        # have, need = 0, len(counT)

        # l = 0
        # res, reslen = [-1, -1], float("infinity")

        # for r in range(len(s)):
        #     c = s[r]

        #     window[c] = 1 + window.get(c, 0)

        #     if c in counT and window[c] == counT[c]:
        #         have += 1

        #     while have == need:
        #         v = r - l + 1

        #         if v < reslen:
        #             reslen = v

        #             res = [l, r]

        #         window[s[l]] -= 1

        #         if s[l] in counT and window[s[l]] < counT[s[l]]:
        #             have -= 1

        #         l += 1

        # return s[res[0] : res[1] + 1] if reslen != float("infinity") else ""