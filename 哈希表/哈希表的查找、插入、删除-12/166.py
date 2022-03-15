class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        s = []
        if (numerator < 0) != (denominator < 0):
            s.append('-')

        # 整数部分
        numerator = abs(numerator)
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.append(str(integerPart))
        s.append('.')

        # 小数部分
        indexMap = {}
        reminder = numerator % denominator
        while reminder and reminder not in indexMap:
            indexMap[reminder] = len(s)
            reminder *= 10
            s.append(str(reminder // denominator))
            reminder %= denominator
        if reminder:  # 有循环节
            insertIndex = indexMap[reminder]
            s.insert(insertIndex, '(')
            s.append(')')
        return "".join(s)