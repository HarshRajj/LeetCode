class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        ans = []
        for ind, val in enumerate(groupSizes) :
            if val not in d :
                d[val] = []
            d[val].append(ind)
            if len(d[val])==val :
                ans.append(d[val])
                d[val] = []
        return ans
            

        