# Time Complexity : O(N * N * N)
# Space Complexity: O(N)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(num, nums, target):
            result = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum == target:
                        result.append([num, nums[left], nums[i], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1
            return result
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            result = result + threeSum(nums[i], nums[i+1:], target-nums[i])
        return result