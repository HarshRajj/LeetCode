class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = Counter(arr)
        
        a = set(s.values())

        return len(s)==len(a)

        