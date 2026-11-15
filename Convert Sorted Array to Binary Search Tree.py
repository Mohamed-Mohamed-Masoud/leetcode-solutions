# Intuition:
# A height-balanced BST needs the left and right subtrees to have almost
# the same size. Since the array is already sorted, picking the middle
# element as the root puts smaller values on its left and larger values
# on its right, which satisfies the BST property. Repeating this on each
# half keeps the tree balanced at every level.
#
# Approach:
# 1. Define a helper createNode(low, high) that builds a subtree from
#    nums[low..high].
# 2. Base case: if low > high, the range is empty, so return None.
# 3. Pick mid = (low + high) // 2 as the root value.
# 4. Recursively build the left subtree from [low, mid - 1] and the
#    right subtree from [mid + 1, high].
# 5. Create TreeNode(nums[mid], left, right) and return it.
# 6. Start the recursion with createNode(0, len(nums) - 1).
#
# Complexity:
# Time:  O(n) -- every element becomes exactly one node.
# Space: O(log n) -- recursion depth equals the tree height, which is
#        log n because the tree is balanced. The output tree itself
#        is not counted.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def createNode(low, high):
            if low > high:
                return
            mid = (low + high) // 2
            left = createNode(low, mid - 1)
            right = createNode(mid + 1, high)
            return TreeNode(nums[mid], left, right)
        return createNode(0, len(nums) - 1)