class Solution:
    from collections import Counter
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #9:25 -> 
        #c = Counter(nums)
        #return [x[0] for x in c.most_common(k)]
        d = defaultdict(int)
        # go through the loop and keep the dictionary
        for el in nums:
            d[el] +=1
        #print(d)
        ls = sorted(d.items(), key= lambda x: x[1], reverse=True)[:k]
        #print(ls)
        return [x[0] for x in ls]


         
         