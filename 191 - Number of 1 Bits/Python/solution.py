class Solution:
    def hammingWeight(self, n: int) -> int:
        ones_count = 0

        while n != 0:
            if n & 1:
                ones_count += 1
            n = n >> 1
        return ones_count
