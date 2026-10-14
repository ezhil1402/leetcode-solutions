class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num or sum < 0:
            return ""
        res = []
        for i in range(num):
            val = min(9, sum)
            res.append(str(val))
            sum -= val
        if sum > 0:
            return "" 
        return "".join(res)