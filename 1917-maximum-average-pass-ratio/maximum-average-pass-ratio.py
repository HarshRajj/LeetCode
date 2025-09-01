import heapq
from typing import List

class Solution:
  def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    
    def calculate_profit(p, t):
      return (p + 1) / (t + 1) - p / t

    max_heap = []
    for i, (p, t) in enumerate(classes):
      if p < t:
        heapq.heappush(max_heap, (-calculate_profit(p, t), i))

    for _ in range(extraStudents):
      
      if not max_heap:
        break
      
      neg_profit, index = heapq.heappop(max_heap)

      classes[index][0] += 1
      classes[index][1] += 1
      
      p, t = classes[index]
      if p < t:
          heapq.heappush(max_heap, (-calculate_profit(p, t), index))

    total_ratio = sum(p / t for p, t in classes)


    return total_ratio / len(classes)