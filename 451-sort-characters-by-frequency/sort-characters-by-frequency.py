class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s) 
        pq = [(-freq, char) for char, freq in dic.items()]
        heapq.heapify(pq)
        result = ''
        while pq :
            freq, char = heapq.heappop(pq)
            result += char*(-freq)
        return result
        

        