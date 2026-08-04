"""
Intuition
The array is rotated but consists of two sorted halves. We can use Binary Search to achieve O(log n) time by identifying which half is strictly sorted and checking if the target belongs in that range.

Approach
1. Initialize `left` and `right` pointers.
2. Check if the target is at the boundaries (`left` or `right`) to handle edge cases quickly.
3. Break the loop if pointers become adjacent (`right - left <= 1`) to prevent infinite loops.
4. Calculate the `mid` index.
5. Determine which part of the array (left or right) is properly sorted.
6. Narrow down the search space by checking if the target falls within the sorted segment's range.

Complexity
- Time complexity: O(log n)
- Space complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if right - left <= 1:
                break
            mid = left + (right - left) // 2
            if nums[left] < nums[mid]:
                if target > nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < nums[right]:
                if target >= nums[mid] and target < nums[right]:
                    left = mid
                else:
                    right = mid
        return -1