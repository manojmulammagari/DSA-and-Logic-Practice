class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        c={}

        for i in strs:

          d="".join(sorted(i))

          if d not in c:
            c[d]=[]

          c[d].append(i)


        return list(c.values())
         


