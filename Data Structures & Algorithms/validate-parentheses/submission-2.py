class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        paranthesis = { ")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in paranthesis:
                if stack and stack[-1] == paranthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

# Time Complexity : o(n)
# Space Complexity : o(n)