# Time Complexity : O(N)
# Space Complexity: O(N)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_dict = {}
        for i, num in enumerate(nums):
            if num in seen_dict and i <= seen_dict[num] + k:
                return True
            else:
                seen_dict[nums[i]] = i
        return False
        