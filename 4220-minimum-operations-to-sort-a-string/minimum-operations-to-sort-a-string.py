class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        min_only_last = (s[-1] == mn and s.count(mn) == 1)
        max_only_first = (s[0] == mx and s.count(mx) == 1)
        if not (min_only_last and max_only_first):
            return 2
        return 3