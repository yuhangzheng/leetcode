# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 递归
        # if not head: return
        # head.next = self.removeElements(head.next, val)
        # return head.next if head.val == val else head

        # 迭代
        # while head and head.val == val:
        #     head = head.next
        # if not head: return
        # pre = head
        # while pre.next:
        #     if pre.next.val == val:
        #         pre.next = pre.next.next
        #     else:
        #         pre = pre.next
        # return head

        # # 双指针
        # while head and head.val == val:
        #     head = head.next
        # pre, cur = head, head
        # while cur:
        #     if cur.val == val:
        #         pre.next = cur.next
        #     else:
        #         pre = cur
        #     cur = cur.next

        # return head

        # 虚拟头结点
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
