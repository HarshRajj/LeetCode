class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
          return abs(cards[0] - 24) < 1e-6
        n = len(cards)
        for i in range(n):
          for j in range(n):
            if i != j:
              new_card = [cards[k] for k in range(n) if k != i and k != j]
              new_num = [cards[i] + cards[j], cards[i] - cards[j], cards[i] * cards[j]]
              if cards[j] != 0:
                new_num.append(cards[i] / cards[j])
              for num in new_num:
                if self.judgePoint24(new_card + [num]):
                  return True
        return False