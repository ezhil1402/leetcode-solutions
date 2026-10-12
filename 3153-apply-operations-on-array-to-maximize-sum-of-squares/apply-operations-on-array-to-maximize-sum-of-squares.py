class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        for x in nums:
            for i in range(32):
                if (x >> i) & 1:
                    bit_counts[i] += 1
        final_nums = [0] * len(nums)
        for i in range(32):
            for j in range(bit_counts[i]):
                final_nums[j] |= (1 << i)
        final_nums.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans = (ans + (final_nums[i] ** 2) % MOD) % MOD
        ans %= MOD
        return ans