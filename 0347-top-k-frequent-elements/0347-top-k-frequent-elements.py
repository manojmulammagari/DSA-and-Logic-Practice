
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=  {}
        freq=[[] for i in range(len(nums)+1)]

        for n in nums:
            c[n]=1+c.get(n,0)
        for n,c in c.items():
            freq[c].append(n)

        res=[]

        for i in range(len(freq)-1,0,-1):

            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res




        
