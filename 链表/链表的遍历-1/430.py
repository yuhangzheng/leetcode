"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Node") -> "Node":
        # def dfs(node: "Node") -> "Node":
        #     cur = node
        #     # 记录链表的最后一个节点
        #     last = None

        #     while cur:
        #         nxt = cur.next
        #         # 如果有子节点，那么首先处理子节点
        #         if cur.child:
        #             child_last = dfs(cur.child)

        #             nxt = cur.next
        #             # 将 node 与 child 相连
        #             cur.next = cur.child
        #             cur.child.prev = cur

        #             # 如果 nxt 不为空，就将 last 与 nxt 相连
        #             if nxt:
        #                 child_last.next = nxt
        #                 nxt.prev = child_last

        #             # 将 child 置为空
        #             cur.child = None
        #             last = child_last
        #         else:
        #             last = cur
        #         cur = nxt

        #     return last

        # dfs(head)
        # return head

        curr = head
        while curr:
            if curr.child:
                nex = curr.next
                child = curr.child

                # 遇到一个child，先在 curr 这里豁开一个口子，把child变成 next 的关系
                curr.next = child
                curr.child = None
                child.prev = curr

                # 找到当前这个child链的最末尾
                while child.next:
                    child = child.next
                # 把child的最末尾的节点，跟上面豁开的口子 nex 接上
                if nex:
                    nex.prev = child
                child.next = nex
            curr = curr.next
        return head

