# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if not head:
        #     return head

        # l = dummy = ListNode(0, head)
        # r = head

        # flag = 1
        # while l.next !=None and l.next.next != None:
        #     l.next = r.next
        #     tmp = r.next.next
        #     r.next.next = r
        #     r.next = tmp
        #     l = r
        #     r = tmp
        # return dummy.next

        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead