class Solution:
    def pickGifts(self, gifts: List[int], k: int)->int :
        for i in range(k) :
            gifts.sort()
            gifts[-1] = int(sqrt(gifts[-1]))
        return sum(gifts)


        