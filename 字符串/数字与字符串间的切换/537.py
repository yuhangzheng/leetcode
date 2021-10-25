class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = num1.split("+")
        c, d = num2.split("+")
        b = b[:len(b)-1]
        d = d[:len(d)-1]
        num1 = int(a) * int(c) - int(b) * int(d)
        num2 = int(a) * int(d) + int(b) * int(c)
        return str(num1) + "+" + str(num2) + "i"