from typing import List

import base64

class Codec:

    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        path = base64.urlsafe_b64encode(abs(hash(longUrl)).to_bytes(8, 'little')).decode('ascii')
        self.urls[path] = longUrl
        return "http://tinyurl.com/" + path


    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl[19:]]

if __name__ == "__main__":
    s = Solution()
    print(s.solution())

