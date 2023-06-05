# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 如果 a=ba=b，则两个指针会同时到达两个链表相交的节点，此时返回相交的节点；
        # 如果 a !=b，则指针 \textit{pA}pA 会遍历完链表 \textit{headA}headA，指针 \textit{pB}pB
        # 会遍历完链表 \textit{headB}headB，两个指针不会同时到达链表的尾节点，然后指针 \textit{pA}pA
        #移到链表 \textit{headB}headB 的头节点，指针 \textit{pB}pB 移到链表 \textit{headA}headA
        # 的头节点，然后两个指针继续移动，在指针 \textit{pA}pA 移动了 a+c+b 次、
        #指针 \textit{pB}pB 移动了 b+c+a 次之后，两个指针会同时到达两个链表相交的节点，
        #该节点也是两个指针第一次同时指向的节点，此时返回相交的节点。
        if not headA or not headB:
            return None
        p = headA
        q = headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p