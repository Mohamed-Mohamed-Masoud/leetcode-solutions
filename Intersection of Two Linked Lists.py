# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = xhttps://leetcode.com/problems/intersection-of-two-linked-lists/$0
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return None
        point_A = headA
        point_B = headB
        while point_A != point_B:
            point_A = point_A.next if point_A else headB
            point_B = point_B.next if point_B else headA
        return point_A