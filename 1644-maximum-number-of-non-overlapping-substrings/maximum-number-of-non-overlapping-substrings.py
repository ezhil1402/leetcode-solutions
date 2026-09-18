class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i
        intervals = []
        for c in range(26):
            if first[c] == n:
                continue
            l = first[c]
            r = last[c]
            i = l
            valid = True
            while i <= r:
                x = ord(s[i]) - ord('a')
                if first[x] < l:
                    valid = False
                    break
                r = max(r, last[x])
                i += 1
            if valid:
                intervals.append((l, r))
        intervals.sort(key=lambda x: x[1])
        result = []
        end = -1
        for l, r in intervals:
            if l > end:
                result.append(s[l:r + 1])
                end = r
        return result