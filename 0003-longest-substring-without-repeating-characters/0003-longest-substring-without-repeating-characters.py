class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c={}
        left=0
        ml=0

        for i,n in enumerate(s):
            while n in c and c[n]>=left:
                left=c[n]+1

            c[n]=i

            ml=max(ml,i-left+1)

        return ml
    
        