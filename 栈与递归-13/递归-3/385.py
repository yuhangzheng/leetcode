# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # def dfs(elem):
        #     if type(elem) == int:
        #         return NestedInteger(elem)
        #     li = NestedInteger()  # 这个对象为空时是一个空列表
        #     for i in elem:
        #         li.add(dfs(i))
        #     return li
        # return dfs(eval(s))

        # 如果第一个字符不是“【”，直接返回
        if s[0] != "[":
            return NestedInteger(int(s))

        if s == "[]":
            return NestedInteger()

        stack = []
        tmp_num = ""
        for i, cha in enumerate(s):

            # 每当遇到一个“【”，意味着有一个NestedInteger对象
            if cha == "[":
                stack.append(NestedInteger())

            elif cha == ",":
                if s[i - 1] != "]":
                    # 前面是数字时才执行
                    num = int(tmp_num)
                    stack[-1].add(NestedInteger(num))
                    tmp_num = ""

            elif cha == "]":
                # 前面是数字时才执行
                if s[i - 1] != "]":
                    if s[i - 1] != "[":
                        num = int(tmp_num)
                        stack[-1].add(NestedInteger(num))

                # 如果stack中只剩下一个对象，则嵌套结束，
                if len(stack) > 1:
                    top = stack.pop()
                    stack[-1].add(top)
                tmp_num = ""

            # 对数字的处理
            else:
                tmp_num += cha

        return stack[0]