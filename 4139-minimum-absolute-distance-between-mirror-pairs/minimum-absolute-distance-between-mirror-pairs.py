class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dic = {}
        dist = float('inf')

        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])

            if num in dic :
                cur = i - dic[num]

                if cur < dist :
                    dist = cur

            dic[rev] = i

        return -1 if dist == float('inf') else dist

                    
        