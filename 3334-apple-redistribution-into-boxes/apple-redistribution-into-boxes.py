class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        total = sum(apple)
        for i,x in enumerate(sorted(capacity, reverse = True)) :
            total -= x 
            if total <= 0 : return i+1 
        return -1
        