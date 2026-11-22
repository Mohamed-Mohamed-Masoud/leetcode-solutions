# Intuition:
# Since the array is sorted and has unique values, a range is just a run
# of consecutive numbers (each one equal to the previous + 1). We scan
# once while tracking the start (l) and end (h) of the current run.
# When the run breaks, we write it out as either "a" or "a->b" and
# start a new run.
#
# Approach:
# 1. If nums is empty, return an empty list.
# 2. Set l and h (start and end of the current range) to nums[0].
# 3. For each i from 1 to len(nums) - 1:
#    - If nums[i] == nums[i-1] + 1, the range continues, so set
#      h = nums[i] and move on.
#    - Otherwise the range ended. If l == h, append str(l);
#      else append "l->h".
#    - Start a new range with l = h = nums[i].
# 4. After the loop, the last range hasn't been added yet, so append it
#    using the same l == h check.
# 5. Return result.
#
# Complexity:
# Time:  O(n) -- a single pass over the array.
# Space: O(1) -- only a few variables are used. The output list is not
#        counted.

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        l = nums[0]
        h = nums[0]
        result = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                h = nums[i]
                continue
            elif l == h:
                result.append(str(l))
            else:
                result.append(str(l) + '->' + str(h))
            l = nums[i]
            h = l
        result.append(str(l)) if l == h else result.append(str(l) + '->' + str(h))
        return result