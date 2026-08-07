
class Solution(object):
    @classmethod
    def isValid(cls, s):
        stack = []
        valid = {
    "(": ")",
    "{": "}",
    "[": "]"
}
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack or char != valid[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0

print(Solution.isValid("()"))       
print(Solution.isValid("()[]{}"))   
print(Solution.isValid("(]"))   
print(Solution.isValid("(("))       
print(Solution.isValid(")"))        