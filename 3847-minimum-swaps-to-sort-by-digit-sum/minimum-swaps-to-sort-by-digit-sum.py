class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        # Sort by digit sum, then by integer value
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its original index
        index = {num: i for i, num in enumerate(nums)}

        # Find the minimum swaps using cycle detection
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or index[sorted_nums[i]] == i:
                visited[i] = True
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = index[sorted_nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps