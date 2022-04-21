from typing import List

import random

SET_SIZE = int(10 ** 4)

def hash(i):
    random.seed(i)
    return random.randint(0, SET_SIZE - 1)

class MyHashSet:
    def __init__(self):
        self.lst = [[] for i in range(SET_SIZE)]

    def add(self, key: int) -> None:
        h = hash(key)
        if not key in self.lst[h]:
            self.lst[h].append(key)


    def remove(self, key: int) -> None:
        h = hash(key)
        if key in self.lst[h]:
            self.lst[h].remove(key)


    def contains(self, key: int) -> bool:
        h = hash(key)
        return key in self.lst[h]


if __name__ == "__main__":
    s = MyHashSet()

    for
