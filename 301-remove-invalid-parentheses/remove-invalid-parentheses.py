class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_rem = 0
        right_rem = 0
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1
        res = set()
        def backtrack(index: int, left_count: int, right_count: int, left_rem: int, right_rem: int, path: list):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.add("".join(path))
                return
            char = s[index]
            if char == '(' and left_rem > 0:
                backtrack(index + 1, left_count, right_count, left_rem - 1, right_rem, path)
            elif char == ')' and right_rem > 0:
                backtrack(index + 1, left_count, right_count, left_rem, right_rem - 1, path)
            path.append(char)
            if char != '(' and char != ')':
                backtrack(index + 1, left_count, right_count, left_rem, right_rem, path)
            elif char == '(':
                backtrack(index + 1, left_count + 1, right_count, left_rem, right_rem, path)
            elif char == ')' and left_count > right_count:
                backtrack(index + 1, left_count, right_count + 1, left_rem, right_rem, path)
            path.pop()
        backtrack(0, 0, 0, left_rem, right_rem, [])
        return list(res)