class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                distinct_count = len(seen)
                total_sum += distinct_count ** 2    
        return total_sum