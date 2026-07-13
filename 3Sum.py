# Time Complexity : O(N * N)
# Space Complexity: O(N)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum == 0:
                        result.append([nums[left], nums[i], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum > 0:
                        right -= 1
                    else:
                        left += 1
        return result