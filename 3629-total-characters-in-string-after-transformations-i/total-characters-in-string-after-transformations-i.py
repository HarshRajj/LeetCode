class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        mp = Counter(s)  

        for _ in range(t):  
            temp = {}
            for ch, freq in mp.items():
                if ch != 'z':
                    next_char = chr(ord(ch) + 1)
                    temp[next_char] = (temp.get(next_char, 0) + freq) % MOD
                else:
                    temp['a'] = (temp.get('a', 0) + freq) % MOD
                    temp['b'] = (temp.get('b', 0) + freq) % MOD
            mp = temp  

        return sum(mp.values()) % MOD  
