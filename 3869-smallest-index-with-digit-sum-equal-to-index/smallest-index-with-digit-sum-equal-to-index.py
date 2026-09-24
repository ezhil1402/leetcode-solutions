class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            digit_sum = sum(int(digit) for digit in str(num))
            if digit_sum == i:
                return i
        return -1