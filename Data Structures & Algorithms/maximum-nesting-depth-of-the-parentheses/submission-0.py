class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []

        for ch in s:
            if ch == "(":
                stack.append("(")
                res = max(res, len(stack))
            elif ch == ")" and stack[-1]:
                stack.pop()

        return res