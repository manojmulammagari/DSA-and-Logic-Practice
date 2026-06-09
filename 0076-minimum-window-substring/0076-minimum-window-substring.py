class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if s is "" or t is "" or len(s)<len(t):
            return ""

        tar_cou = Counter(t)

        uni = len(tar_cou)

        window = {}

        left = 0

        form_char = 0

        min_len = len(s)+1

        bestleft = 0

        bestright = 0

        for right in range(len(s)):
            cr = s[right]
            window[cr] = window.get(cr,0)+1

            if cr in tar_cou and window[cr] == tar_cou[cr]:
                form_char = form_char + 1

            while form_char == uni:
                curlen = right - left +1

                if curlen < min_len:
                    min_len = curlen
                    bestleft = left
                    bestright = right

                charl = s[left]

                window[charl] = window.get(charl,0)-1

                if charl in tar_cou and window[charl]<tar_cou[charl]:
                    form_char = form_char - 1

                left = left + 1

        if min_len == len(s)+1:
            return ""

        else:
            return s[bestleft : bestright + 1]
