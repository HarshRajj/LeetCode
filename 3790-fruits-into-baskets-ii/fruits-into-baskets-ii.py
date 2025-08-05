class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        ans = n  # assume all are unplaced initially

        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    ans -= 1  
                    baskets[j] = 0  
                    break

        return ans