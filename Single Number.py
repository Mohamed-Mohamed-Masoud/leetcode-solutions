# Intuition:
# XOR has two key properties: a ^ a = 0 and a ^ 0 = a. It is also
# commutative and associative, so the order doesn't matter. When we XOR
# all the numbers together, every number that appears twice cancels
# itself out, and only the number that appears once remains.
#
# Approach:
# 1. Initialize result to 0.
# 2. Loop over each number in nums and XOR it into result.
# 3. Pairs of equal numbers cancel to 0, so after the loop result
#    holds the single number. Return it.
#
# Complexity:
# Time:  O(n) -- a single pass over the array.
# Space: O(1) -- only one variable is used, no hash table needed.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result