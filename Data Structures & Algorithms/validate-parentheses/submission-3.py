class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        b = {")":"(", "}":"{", "]":"["}
        o = "([{"
        stack = []

        for i in s:
            if i in o:
                stack.append(i)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if top != b[i]:
                    return False

        return len(stack) == 0
            