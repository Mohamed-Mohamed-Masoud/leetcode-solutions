"""
Intuition
In a preorder traversal, the first element is always the root of the current tree. By locating this root value within the inorder traversal, we can determine the exact boundaries of the left and right subtrees. Using a Hash Map to store the indices of the inorder array allows us to perform these lookups in constant time, optimizing the tree construction.

Approach
1. Create a hash dictionary `inorder_dict` to map each value in the `inorder` array to its corresponding index.
2. Initialize a pointer `val_index` to keep track of the current root element in the `preorder` array.
3. Define a recursive helper function `array_to_tree(left, right)` to construct the tree within the current boundaries of the inorder array.
4. Base case: If `left > right`, there are no elements to form a subtree, so return `None`.
5. Retrieve the current root value from `preorder[val_index]`, increment `val_index`, and instantiate a new `TreeNode`.
6. Look up the index of this root value (`mid`) in `inorder_dict`.
7. Recursively build the `left` child using the elements strictly to the left of `mid` (from `left` to `mid - 1`).
8. Recursively build the `right` child using the elements strictly to the right of `mid` (from `mid + 1` to `right`).
9. Return the constructed root node and initiate the recursion with the full array bounds `(0, len(inorder) - 1)`.

Complexity
- Time complexity: O(N) where N is the number of nodes in the tree. Building the hash map takes O(N) time, and we visit each node exactly once during recursion with O(1) hash map lookups.
- Space complexity: O(N) to store the hash map mapping all N elements. The recursion stack will also use O(N) space in the worst-case scenario (a completely skewed tree), or O(log N) for a balanced tree.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val:i for i,val in enumerate(inorder)}
        val_index = 0
        
        def array_to_tree(left, right):
            nonlocal val_index
            if left > right:
                return None
            
            val = preorder[val_index]
            val_index += 1
            mid = inorder_dict[val]
            
            return TreeNode(val, array_to_tree(left, mid-1), array_to_tree(mid+1, right))
            
        return array_to_tree(0, len(inorder)-1)