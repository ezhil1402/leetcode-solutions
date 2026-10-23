from typing import List
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        misplaced = [num for i, num in enumerate(nums) if i != num]
        if not misplaced:
            return 0
        ans = misplaced[0]
        for num in misplaced[1:]:
            ans &= num
        return ans