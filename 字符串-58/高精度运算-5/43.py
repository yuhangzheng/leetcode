class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = self.addStrings(ans, curr)
        return ans

    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        f1 = 1
        ans = 0
        # 倒序遍历
        for i in range(len(num1)-1,-1,-1):
            # 进位数
            f2 = 1
            # n1 乘以进位数
            n1 = int(num1[i]) * f1

            # 倒序遍历
            for j in range(len(num2)-1,-1,-1):
                n2 = int(num2[j]) * f2
                ans += n1 * n2

                # 进位数处理 *10
                f2 *=10
            f1 *=10
        return str(ans)