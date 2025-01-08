class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        prev = pref[0]
        for i in range(1, n):
            temp = pref[i]
            pref[i] ^= prev
            prev = temp
        return pref
