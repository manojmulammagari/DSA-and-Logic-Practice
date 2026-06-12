class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == "" or t == "" or len(s) < len(t):
            return ""

        counT, window = Counter(t), {}

        have, need = 0, len(counT)

        l = 0
        res, reslen = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            if c in counT and window[c] == counT[c]:
                have += 1

            while have == need:
                v = r - l + 1

                if v < reslen:
                    reslen = v

                    res = [l, r]

                window[s[l]] -= 1

                if s[l] in counT and window[s[l]] < counT[s[l]]:
                    have -= 1

                l += 1

        return s[res[0] : res[1] + 1] if reslen != float("infinity") else ""