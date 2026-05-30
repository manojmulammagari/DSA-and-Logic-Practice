class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        c=defaultdict(list)

        for s in strs:

            v="".join (sorted(s))

            c[v].append(s)

        return list(c.values())

          



