class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = []
        
        for i in nums:
            a = [] 
            for d in str(i):
                a.append(int(d))
            mini.append(sum(a))
            
        return min(mini)