class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        res = 0
        i = 0
        while i < len(tokens):
            if tokens[i] in ['+', '-', '*', '/']:
                b = int(s.pop())
                a = int(s.pop())
                if tokens[i] == '+':
                    res = a + b
                elif tokens[i] == '-':
                    res = a - b
                elif tokens[i] == "*":
                    res = a * b
                else:
                    res = a/b
                
                s.append(res)
            else:
                s.append(tokens[i])
            i += 1

        return int(s.pop())
                