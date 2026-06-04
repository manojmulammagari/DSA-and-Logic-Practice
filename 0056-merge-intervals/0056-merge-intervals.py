class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x:x[0])


        merge=[]

        for x in intervals:

            if not merge or merge[-1][1]<x[0]:

                merge.append(x)

            else:
                merge[-1][1] = max(merge[-1][1],x[1])

        return merge