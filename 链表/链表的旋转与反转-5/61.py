# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if k == 0 or not head or not head.next:
        #     return head
        # n = 1
        # cur = head
        # while cur.next:
        #     cur = cur.next
        #     n += 1

        # if k % n == 0:
        #     return head

        # k_2 = k % n
        # p = q = head
        # for i in range(k_2):
        #     q = q.next
        # while q.next:
        #     p = p.next
        #     q = q.next
        # q.next = head
        # hd = p.next
        # p.next = None
        # head = hd
        # return head

        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        if (add := n - k % n) == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret