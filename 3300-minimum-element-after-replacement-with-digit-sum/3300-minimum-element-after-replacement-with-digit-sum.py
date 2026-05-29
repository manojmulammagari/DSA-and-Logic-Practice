class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=[]

        for i in nums:

            a=[]
            for b in str(i):
                a.append(int(b))

            mini.append(sum(a))
                

        return min(mini)