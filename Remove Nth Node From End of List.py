"""
Intuition:
To find the Nth node from the end in a single pass, we can maintain a gap of 'n' nodes between two pointers. 
When the leading pointer reaches the end, the trailing pointer will be right before the target node.

Approach:
1. Use a dummy node pointing to the head to simplify edge cases (e.g., removing the head itself).
2. Set 'slow_node' at the dummy and 'fast_node' at the head (dummy.next).
3. Advance 'fast_node' by 'n' steps to create the required gap.
4. Move both pointers forward simultaneously until 'fast_node' reaches the end (None).
5. 'slow_node' is now just before the node to remove; bypass it by updating 'slow_node.next'.

Complexity:
- Time: O(N) where N is the number of nodes in the linked list (One-pass solution).
- Space: O(1) as it only uses two pointers, requiring constant extra space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        slow_node = dummy
        fast_node = dummy.next
        
        for _ in range(n):
            fast_node = fast_node.next
            
        while fast_node:
            slow_node = slow_node.next
            fast_node = fast_node.next
            
        slow_node.next = slow_node.next.next
        
        return dummy.next