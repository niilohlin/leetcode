from typing import List

import random

SET_SIZE = int(10 ** 4)

def hash(i):
    random.seed(i)
    return random.randint(0, SET_SIZE - 1)

class MyHashMap:
    def __init__(self):
        self.lst = [[] for i in range(SET_SIZE)]

    def put(self, key: int, value: int) -> None:
        h = hash(key)

        for i, tuple in enumerate(self.lst[h]):
            k, v = tuple
            if k == key:
                self.lst[h][i] = (key, value)
                return
        self.lst[h].append((key, value))

    def get(self, key: int) -> int:
        h = hash(key)
        for k, v in self.lst[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = hash(key)
        for i, tuple in enumerate(self.lst[h]):
            k, v = tuple
            if k == key:
                self.lst[h].remove((k, v))
                return

if __name__ == "__main__":
    s = MyHashMap()

if __name__ == "__main__":
    s = Solution()
    print(s.solution())
