# Intuition:
# I used the sliding window technique to find the minimum size subarray with a sum greater than or equal to the target.

# Approach:
# 1. Use two pointers, left and right, to maintain a sliding window.
# 2. Expand the window by moving the right pointer and add elements to the current sum.
# 3. When the current sum is greater than or equal to the target, update the minimum length and shrink the window from the left.

# Complexity:
# Time complexity: O(N), where N is the length of the array.
# Space complexity: O(1).


# Code
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                current_length = right - left + 1
                min_length = min(current_length, min_length)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0