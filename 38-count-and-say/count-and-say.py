class Solution:
    def countAndSay(self, n: int) -> str:

        def fn(s)-> str:
            res = []
            cnt = 1

            for i in range(1, len(s)) :
                if s[i] == s[i-1]:
                    cnt += 1
                else:
                    res.append(f"{cnt}{s[i-1]}")
                    cnt = 1

            res.append(f"{cnt}{s[-1]}")
            return "".join(res)

        res = "1"
        for _ in range(n-1):
            res = fn(res)
        return res
        