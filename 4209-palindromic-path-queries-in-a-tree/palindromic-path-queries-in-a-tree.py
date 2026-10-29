class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict

        # Build the tree
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # HLD arrays
        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # Iterative DFS to avoid recursion depth issues
        order = [0]
        parent[0] = 0

        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        # Calculate subtree sizes and heavy children
        for u in reversed(order):
            max_size = 0
            for v in adj[u]:
                if v != parent[u]:
                    size[u] += size[v]
                    if size[v] > max_size:
                        max_size = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0

        # Assign heavy chains and positions
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # Each character is represented by one bit
        values = [1 << (ord(s[u]) - ord('a')) for u in range(n)]

        # Segment tree supporting XOR updates and range queries
        class SegmentTree:
            def __init__(self, arr):
                self.n = len(arr)
                self.tree = [0] * (2 * self.n)

                for i, value in enumerate(arr):
                    self.tree[self.n + i] = value

                for i in range(self.n - 1, 0, -1):
                    self.tree[i] = self.tree[2 * i] ^ self.tree[2 * i + 1]

            def update(self, index, value):
                index += self.n
                self.tree[index] = value

                while index > 1:
                    index //= 2
                    self.tree[index] = (
                        self.tree[2 * index] ^ self.tree[2 * index + 1]
                    )

            def query(self, left, right):
                # Inclusive range [left, right]
                left += self.n
                right += self.n + 1
                result = 0

                while left < right:
                    if left & 1:
                        result ^= self.tree[left]
                        left += 1

                    if right & 1:
                        right -= 1
                        result ^= self.tree[right]

                    left //= 2
                    right //= 2

                return result

        base = [0] * n
        for u in range(n):
            base[pos[u]] = values[u]

        seg = SegmentTree(base)

        def path_mask(u, v):
            mask = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                mask ^= seg.query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            mask ^= seg.query(pos[u], pos[v])
            return mask

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                values[u] = 1 << (ord(c) - ord('a'))
                seg.update(pos[u], values[u])

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_mask(u, v)

                # At most one character may have an odd frequency
                answer.append((mask & (mask - 1)) == 0)

        return answer