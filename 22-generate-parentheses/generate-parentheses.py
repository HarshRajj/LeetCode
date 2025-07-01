from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curr: List[str], open_count: int, close_count: int):
            if len(curr) == 2 * n:
                result.append("".join(curr))
                return

            if open_count < n:
                curr.append("(")
                backtrack(curr, open_count + 1, close_count)
                curr.pop()

            if close_count < open_count:
                curr.append(")")
                backtrack(curr, open_count, close_count + 1)
                curr.pop()

        backtrack([], 0, 0)
        return result
