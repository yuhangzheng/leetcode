# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.l = []

        # 递归函数
        def pending_nums(nestedList):
            # 对于nestedList的每个元素进行遍历
            for element in nestedList:
                # 如果这个元素是单个的数字则保存在我们的列表中
                if element.isInteger():
                    self.l.append(element.getInteger())
                # 如果这个元素不是数字而是nestedList
                else:
                    # 获取当前的nestedList
                    eeNest = element.getList()
                    # 进行重复递归即可
                    pending_nums(eeNest)

        pending_nums(nestedList)
        # 当前访问索引
        self.index = 0
        # 总的数字个数
        self.lenth = len(self.l)

    def next(self) -> int:
        # 返回当前索引的元素值，索引+1
        value = self.l[self.index]
        self.index += 1
        return value

    def hasNext(self) -> bool:
        # 根据索引和列表长判断是否还有下一个元素
        return self.index < self.lenth

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())