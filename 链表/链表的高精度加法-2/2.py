# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # p = l1
        # q = l2
        # add = 0
        # while p != None and q != None:
        #     p.val = p.val + q.val + add
        #     if p.val > 9:
        #         p.val = p.val % 10
        #         add = 1
        #     else:
        #         add = 0
        #     p = p.next
        #     q = q.next
        # while p != None:
        #     p.val = p.val + add
        #     if p.val > 9:
        #         p.val = p.val % 10
        #         add = 1
        #     else:
        #         add = 0
        # while q != None:
        #     p = q

        #     p.val = p.val + add
        #     if p.val > 9:
        #         p.val = p.val % 10
        #         add = 1
        #     else:
        #         add = 0

        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total % 10)
            remainder = total // 10

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next

        if remainder: curr.next = ListNode(remainder)
        return result.next
