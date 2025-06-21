class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        result = float('inf')

        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        for i in range(26):
            freqi = freq[i]
            if freqi == 0:
                continue

            deletions = 0

            for j in range(26):
                if i == j or freq[j] == 0:
                    continue

                if freq[j] < freqi:
                    deletions += freq[j]
                elif freq[j] - freqi > k:
                    deletions += freq[j] - (freqi + k)

            result = min(result, deletions)

        return result
