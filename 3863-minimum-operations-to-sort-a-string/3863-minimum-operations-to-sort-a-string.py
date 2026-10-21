class Solution:
    def minOperations(self, s: str) -> int:
        # 1. If the string is already sorted, 0 operations are needed
        if all(s[i] <= s[i+1] for i in range(len(s) - 1)):
            return 0
            
        # 2. If length is 2 and it's not sorted, it is impossible to sort
        if len(s) == 2:
            return -1
            
        mn = min(s)
        mx = max(s)
        
        # 3. 1 operation: If the minimum char is already at the start OR 
        # the maximum char is already at the end, we just sort the rest of the string.
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # 4. 3 operations: If the ONLY minimum char is at the very end AND 
        # the ONLY maximum char is at the very beginning (e.g., "edc").
        if s.find(mn) == len(s) - 1 and s.rfind(mx) == 0:
            return 3
            
        # 5. 2 operations: All other cases can be sorted by sorting 
        # the prefix (len-1) and then the suffix (len-1), or vice versa.
        return 2