from typing import List

from collections import defaultdict
from itertools import zip_longest

Table = lambda: defaultdict(lambda: "0")

def to_table(n: str) -> Table:
    res = Table()
    for i, x in enumerate(reversed(n)):
        res[i] = x
    return res

def to_s(table: Table) -> str:
    res = ""
    for i, c in sorted(table.items(), reverse=True):
        res += c
    return res

def add(table1: Table, table2: Table) -> Table:
    res = Table()
    i = 0
    remainder = 0
    while i in table1 or i in table2:
        i_res = ord(table1[i]) - ord("0") + ord(table2[i]) - ord("0") + remainder
        remainder = i_res // 10
        res[i] = str(i_res % 10)
        i += 1
    if remainder != 0:
        res[i + 1] = str(remainder)
    return res


def mul(table1: Table, table2: Table) -> Table:
    res = Table()
    for i in table1.keys():
        for j in table2.keys():
            intermediate_table = to_table(str((ord(table1[i]) - ord("0")) * (ord(table2[j]) - ord("0"))))
            for k in intermediate_table.keys():
                # res[i + j + k]

    return res


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

if __name__ == "__main__":
    s = Solution()
    for i in range(1000):
        for j in range(100):
            assert to_s(add(to_table(str(i)), to_table(str(j)))) == str(i + j)
    print(s.multiply("129", "2"))
    # print(s.multiply("123", "456"))
