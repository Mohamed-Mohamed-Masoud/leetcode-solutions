### Intuition
# To find the immediate next lexicographically greater permutation, 
# the modification must happen at the least significant digits (from the right). 
# The main idea is to locate the first element from the right that breaks the descending order. 
# This element represents the position that can be incremented by the smallest possible amount to get the next permutation.

### Approach
# 1. **Find the Pivot:** Traverse the array from right to left to find the first element that is smaller than its immediate right neighbor. 
# 2. **Find the Alter (Successor):** If a pivot is found, traverse from the right side of the array again to find the first element that is strictly greater than the pivot.
# 3. **Swap:** Swap the pivot and the alter to increase the value at the pivot's position by the smallest possible amount.
# 4. **Reverse:** Reverse all elements to the right of the original pivot index. Since they are currently in descending order, reversing them makes them ascending, guaranteeing the smallest possible lexicographical increase.

### Complexity
# - **Time Complexity:** O(N), where N is the length of the array. We iterate through the array at most a couple of times, which takes linear time.
# - **Space Complexity:** O(1), because all modifications are performed in-place without utilizing any extra memory.

### Code

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivot = len(nums) - 2
        
        while pivot >= 0:
            if nums[pivot] < nums[pivot+1]:
                break
            pivot -= 1
            
        alter = len(nums) - 1
        if pivot >= 0:
            while alter > pivot:
                if nums[alter] > nums[pivot]:
                    break
                alter -= 1
            nums[pivot], nums[alter] = nums[alter], nums[pivot]
            
        pivot += 1
        alter = len(nums) - 1
        while alter > pivot:
            nums[pivot], nums[alter] = nums[alter], nums[pivot]
            pivot += 1
            alter -= 1
