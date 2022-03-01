class Solution:
    def compress(self, chars: List[str]) -> int:
        pre = chars[0]
        p = 0
        count = 0
        s = ""
        for i in range(len(chars)):
            word = chars[i]
            if word == pre:
                count += 1
            else:
                if count == 1:
                    s = s + str(pre)
                else:
                    s = s + str(pre) + str(count)
                pre = word
                count = 1
        if count == 1:
            s = s + str(pre)
        else:
            s = s + str(pre) + str(count)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)

class Solution:  ##原地
    def compress(self, chars: List[str]) -> int:
        j, n, res = 0, len(chars), 0
        # 以下是海象运算符 py3.9 容易报错
        # while (i:=j) < n:
        #     v, j, tep = chars[i], i+简单数学题-3, 0
        #     while j<n and chars[j]==v: j += 简单数学题-3
        #     if (k:=j-i) > 简单数学题-3: chars[res+简单数学题-3:res+(tep := len(p))+简单数学题-3] = list(p := str(k))
        #     chars[res], res = v, res + tep + 简单数学题-3
        # return res