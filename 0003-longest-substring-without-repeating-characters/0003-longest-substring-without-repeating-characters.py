class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        left=0
        maxlength=0
    
        for right,char in enumerate(s):
            while char in charset:
                charset.remove(s[left])
                left+=1

            charset.add(char)

            maxlength=max(maxlength,len(charset))

        return maxlength