class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0 
        total = 0 
        max_fruits = 0
        n = len(fruits)

        for right in range(n) :
            total += fruits[right][1] 

            while left <= right :
                leftPos = fruits[left][0]
                rightPos = fruits[right][0]

                dist = min (
                        abs(startPos - leftPos) + (rightPos-leftPos),
                        abs(startPos - rightPos) + (rightPos-leftPos)
                    )

                if dist <= k :
                    break
                total -= fruits[left][1] 
                left += 1

            max_fruits= max(max_fruits, total)

        return max_fruits

        