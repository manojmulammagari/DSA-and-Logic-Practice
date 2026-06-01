class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        
        b = {")": "(", "]": "[", "}": "{"}
        
        
        for char in s:
            if char in b:

                v=stack.pop() if stack else "#"

                if b[char]!=v:
                    return False
            else :

                stack.append(char)
        return len(stack)==0
        


