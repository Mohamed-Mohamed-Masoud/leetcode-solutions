# Approach 1: Pythonic One-Liner (Length Comparison)
# Time Complexity: O(N) | Space Complexity: O(N)
# Note: Very clean, but builds the entire set in memory before comparing.
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# Approach 2: Hash Set with Early Exit (Optimized for Real-World Average Case)
# Time Complexity: O(N) | Space Complexity: O(N)
# Note: Faster in practice because it halts immediately upon finding a duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False