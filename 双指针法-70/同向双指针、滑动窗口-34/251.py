# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = head
        q = head.next
        while q:
            if p.val == q.val:
                q = q.next
                p.next = None
            else:
                p.next = q
                p = p.next
        return head