class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_closing = 0
        for char in s:
            if char == '(':
                if needed_closing % 2 != 0:
                    insertions += 1
                    needed_closing -= 1
                needed_closing += 2
            else:
                needed_closing -= 1
                if needed_closing < 0:
                    insertions += 1
                    needed_closing += 2  
        return insertions + needed_closing