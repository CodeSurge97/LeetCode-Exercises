def isValid(self, s: str) -> bool:
        brack = {'(': ')', '{': '}', '[':']'}
        stack = []
        for i in s:
            if i in brack:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == brack.get(stack[-1]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0