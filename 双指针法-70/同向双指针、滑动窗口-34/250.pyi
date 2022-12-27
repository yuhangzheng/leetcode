# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        virtual = ListNode(0, head)
        p = virtual
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                tmp = p.next.val
                while p.next and p.next.val == tmp:
                    p.next = p.next.next
            else:
                p = p.next
        return virtual.next