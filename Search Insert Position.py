# Intuition:
# The array is sorted, so we don't need to scan every element.
# Binary search halves the search space at each step. If the target
# isn't found, `low` ends up exactly at the position where the
# target should be inserted.
#
# Approach:
# 1. Initialize low = 0 and high = len(nums) - 1.
# 2. While low <= high, compute mid = (low + high) // 2.
# 3. If nums[mid] == target, return mid.
# 4. If nums[mid] < target, search right: low = mid + 1.
# 5. Otherwise, search left: high = mid - 1.
# 6. When the loop ends, the target isn't in the array. `low` is the
#    index of the first element greater than the target, which is the
#    correct insertion position, so return low.
#
# Complexity:
# Time:  O(log n) -- the search range is halved on each iteration.
# Space: O(1)     -- only a few pointers are used.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low