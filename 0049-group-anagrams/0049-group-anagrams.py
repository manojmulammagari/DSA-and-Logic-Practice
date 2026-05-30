class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        c={}

        for s in strs:

            v="".join (sorted(s))

            if v not in c:

                c[v]=[]

            c[v].append(s)

        return list(c.values())

          



