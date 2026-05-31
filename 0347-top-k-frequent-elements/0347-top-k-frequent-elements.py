
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      a={}
      f=[[]for i in range(len(nums)+1)]


      for n in nums:
        a[n]= 1+a.get(n,0)

      for i,n in a.items():
        f[n].append(i)

      res=[]

      for i in range(len(f)-1,0,-1):
        for n in f[i]:
            res.append(n)
            if len(res)==k:
                return res
