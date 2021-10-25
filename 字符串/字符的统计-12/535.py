import random


class Codec:
    _chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _dict = {}
    _key = ''.join(random.sample(_chars, 6))

    def get_rand(self):
        return ''.join(random.sample(self._chars, 6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        """
        将一个 长URL 编码为一个 短URL【随机固定长度加密】。

        使用 random 模块 随机从 62 位字符串中选取 6 个作为 URL短路径。
        因为使用了随机数，根据 short_url 来预测字典大小几乎是不可能的，数据更加安全。
        """
        while self._dict.get(self._key):
            self._key = self.get_rand()

        self._dict[self._key] = longUrl

        return 'http://tinyurl.com/' + self._key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        """
        将一个 短URL 解码为一个 长URL。

        直接根据 url字符串后6位，从字典中取值。
        """
        return self._dict[shortUrl[19:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))