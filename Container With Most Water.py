"""
Intuition:
To maximize the amount of water a container can store, we need to maximize both its width and height. 
Starting with the maximum width (pointers at both ends) allows us to explore the largest possible width first. 
Since the height of the water is determined by the shorter line, moving the pointer of the shorter line inwards 
gives us a chance to find a taller line, potentially increasing the total area despite the reduced width.

Approach:
1. Initialize two pointers: `left` at the beginning (index 0) and `right` at the end (index n-1).
2. Initialize `result` to 0 to keep track of the maximum area found.
3. Iterate using a while loop as long as `left < right`:
   - Calculate the `current_area` by multiplying the distance between the pointers by the minimum height of the two.
   - Update `result` to be the maximum of itself and `current_area`.
   - Move the pointer pointing to the shorter line inward to seek a potentially taller line.
4. Return the `result`.

Complexity:
- Time Complexity: O(N) where N is the number of elements in the height array. The two pointers traverse the array exactly once.
- Space Complexity: O(1) because we only use a few extra variables for pointers and area calculations, requiring no additional scaling memory.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            result = max(result, current_area)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return result