class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
        base = set(guess)
        # cow 为公共集 - 正确集
        for j in base:
            if j in secret:
                b += min(guess.count(j), secret.count(j))
        b = b - a
        return str(a) + 'A' + str(b) + 'B'
