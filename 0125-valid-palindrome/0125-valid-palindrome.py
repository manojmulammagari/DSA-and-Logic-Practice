class Solution:
    def isPalindrome(self, s: str) -> bool:
        v= s.lower()
        seen=[]

        for i in v:
            if i.isalpha() or i.isdigit() :
                seen.append(i)

        for i in range(len(seen)):
            if seen[i] != seen[len(seen)-1-i]:
                return False
        return True
        
            