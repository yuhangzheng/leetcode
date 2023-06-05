# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        f, s = ListNode(), ListNode()
        p, q = f, s
        # 两段链表整理起来
        while head:
            if head.val < x:
                p.next = head
                p = p.next
                head = p.next
            else:
                q .next = head
                q = q.next
                head = q.next
        p.next = s.next
        q.next = None
        return f.next