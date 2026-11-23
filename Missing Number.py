# Intuition:
# The array holds n distinct numbers taken from the range [0, n], so
# exactly one number in that range is missing. If we put all the numbers
# in a hash set, we can check whether each value from 0 to n exists in
# O(1) time. The first value that isn't in the set is the answer.
#
# Approach:
# 1. Convert nums into a set called nums_set for O(1) lookups.
# 2. Loop over every i from 0 to len(nums) (inclusive).
# 3. If i is not in nums_set, it is the missing number, so return it.
# 4. The loop is guaranteed to find one, since exactly one number from
#    the range is absent.
#
# Complexity:
# Time:  O(n) -- building the set takes O(n), and the loop does at most
#        n + 1 lookups of O(1) each.
# Space: O(n) -- the set stores up to n elements.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i