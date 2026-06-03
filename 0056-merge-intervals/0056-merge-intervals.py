class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []

        for x in intervals:
            if not merged or merged[-1][-1] < x[0]:
                merged.append(x)

            else:
                merged[-1][-1] = max(merged[-1][-1], x[1])

        return merged
