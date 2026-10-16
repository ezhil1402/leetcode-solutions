
from typing import List

MOD = 10**9 + 7


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)      # Sum of squares
        self.sum_val = [0] * (4 * n)   # Sum of values
        self.lazy = [0] * (4 * n)      # Pending increments

    def apply(self, node, l, r, val):
        length = r - l + 1

        self.tree[node] = (
            self.tree[node]
            + 2 * val * self.sum_val[node]
            + val * val * length
        ) % MOD

        self.sum_val[node] = (
            self.sum_val[node] + val * length
        ) % MOD

        self.lazy[node] = (self.lazy[node] + val) % MOD

    def push(self, node, l, r):
        if self.lazy[node] == 0 or l == r:
            return

        mid = (l + r) // 2
        val = self.lazy[node]

        self.apply(2 * node, l, mid, val)
        self.apply(2 * node + 1, mid + 1, r, val)

        self.lazy[node] = 0

    def update(self, node, l, r, ql, qr, val):
        if ql > r or qr < l:
            return

        if ql <= l and r <= qr:
            self.apply(node, l, r, val)
            return

        self.push(node, l, r)

        mid = (l + r) // 2

        self.update(2 * node, l, mid, ql, qr, val)
        self.update(2 * node + 1, mid + 1, r, ql, qr, val)

        self.tree[node] = (
            self.tree[2 * node] + self.tree[2 * node + 1]
        ) % MOD

        self.sum_val[node] = (
            self.sum_val[2 * node] + self.sum_val[2 * node + 1]
        ) % MOD


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        seg = SegmentTree(n)

        last_seen = {}
        ans = 0

        for j, x in enumerate(nums):
            last_idx = last_seen.get(x, -1)

            # Increase distinct counts for subarrays
            # ending at index j.
            seg.update(1, 0, n - 1, last_idx + 1, j, 1)

            last_seen[x] = j

            # Sum of squared distinct counts for
            # all subarrays ending at index j.
            ans = (ans + seg.tree[1]) % MOD

        return ans
