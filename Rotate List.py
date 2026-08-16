"""
Intuition:
Rotating a linked list to the right by 'k' places essentially means moving the last 'k' nodes to the front. The most efficient way to achieve this is by connecting the tail to the head to form a circular list, and then breaking the circle at the correct position to form the new head and tail.

Approach:
1. Handle edge cases: If the list is empty, has only one node, or k is 0, return the head as is.
2. Traverse the list to find its total length and locate the original 'tail' node.
3. Calculate the effective number of rotations using modulo (`new_k = k % node_length`). If `new_k` is 0, no rotation is needed.
4. Make the linked list circular by pointing the original `tail.next` to the `head`.
5. Move the tail pointer forward `node_length - new_k` times to reach the new tail of the rotated list.
6. Set the `head` to the new tail's next node, break the circle by setting the new tail's next to `None`, and return the new `head`.

Complexity:
- Time: O(N) - where N is the number of nodes in the linked list. We traverse the list once to find the length and tail, and then partially traverse it again to find the new break point.
- Space: O(1) - as we only use a few pointers without allocating any additional space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
            
        node_length = 1
        tail = head
        
        while tail.next:
            node_length += 1
            tail = tail.next
            
        new_k = k % node_length
        if new_k == 0:
            return head
            
        tail.next = head
        
        for _ in range(node_length - new_k):
            tail = tail.next
            
        head = tail.next
        tail.next = None
        
        return head