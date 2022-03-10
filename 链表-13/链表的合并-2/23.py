# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists: return None
#         n = len(lists) #记录子链表数量
#         return self.mergeSort(lists, 0, n - 1) #调用归并排序函数
#     def mergeSort(self, lists: List[ListNode], l: int, r: int) -> ListNode:
#         if l == r:
#             return lists[l]
#         m = (l + r) // 2
#         L = self.mergeSort(lists, l, m) #循环的递归部分
#         R = self.mergeSort(lists, m + 1, r)
#         return self.mergeTwoLists(L, R) #调用两链表合并函数
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

#         prehead = ListNode(-1)
#         prev = prehead
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 prev.next = list1
#                 list1 = list1.next
#             else:
#                 prev.next = list2
#                 list2 = list2.next
#             prev = prev.next

#         # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
#         prev.next = list1 if list1 is not None else list2

#         return prehead.next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 最小堆
        import heapq #调用堆
        minHeap = []
        for listi in lists:
            while listi:
                heapq.heappush(minHeap, listi.val) #把listi中的数据逐个加到堆中
                listi = listi.next
        dummy = ListNode(0) #构造虚节点
        p = dummy
        while minHeap:
            p.next = ListNode(heapq.heappop(minHeap)) #依次弹出最小堆的数据
            p = p.next
        return dummy.next