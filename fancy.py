from typing import List


from itertools import dropwhile
from collections import defaultdict
class Fancy:
    def __init__(self):
        self.lst = []
        self.op_stack = defaultdict(list)

    def append(self, val: int) -> None:
        self.lst.append(val)

    def addAll(self, inc: int) -> None:
        if self.op_stack[len(self.lst)] and self.op_stack[len(self.lst)][-1][0]:
            self.op_stack[len(self.lst)][-1][0] += inc
        else:
            self.op_stack[len(self.lst)].append([inc, None])

    def multAll(self, m: int) -> None:
        if self.op_stack[len(self.lst)] and self.op_stack[len(self.lst)][-1][1]:
            self.op_stack[len(self.lst)][-1][1] *= m
        else:
            self.op_stack[len(self.lst)].append([None, m])

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.lst):
            return -1
        value = self.lst[idx]
        for i, ops in dropwhile(lambda t: t[0] <= idx, sorted(self.op_stack.items())):
            for op in ops:
                if op[0]:
                    value += op[0]
                elif op[1]:
                    value *= op[1]

        return value % (10 ** 9 + 7)



if __name__ == "__main__":
    actions = ["Fancy","append","append","getIndex","append","getIndex","addAll","append","getIndex","getIndex","append","append","getIndex","append","getIndex","append","getIndex","append","getIndex","multAll","addAll","getIndex","append","addAll","getIndex","multAll","getIndex","multAll","addAll","addAll","append","multAll","append","append","append","multAll","getIndex","multAll","multAll","multAll","getIndex","addAll","append","multAll","addAll","addAll","multAll","addAll","addAll","append","append","getIndex"]
    args = [[],[12],[8],[1],[12],[0],[12],[8],[2],[2],[4],[13],[4],[12],[6],[11],[1],[10],[2],[3],[1],[6],[14],[5],[6],[12],[3],[12],[15],[6],[7],[8],[13],[15],[15],[10],[9],[12],[12],[9],[9],[9],[9],[4],[8],[11],[15],[9],[1],[4],[10],[9]]
    expected = [None,None,None,8,None,12,None,None,24,24,None,None,4,None,12,None,20,None,24,None,None,37,None,None,42,None,360,None,None,None,None,None,None,None,None,None,220560,None,None,None,285845760,None,None,None,None,None,None,None,None,None,None,150746316]
    # actions = ["Fancy", "append", "addAll", "append", "getIndex", "getIndex"]
    # args = [[], [1], [100], [2], [0], [1]]
    # expected = [None, None, None, None, 101, 2]

    fancy = Fancy()

    for action, arg, exp in zip(actions, args, expected):
        if action == "Fancy":
            fancy = Fancy()
        else:
            result = fancy.__getattribute__(action).__call__(arg[0])
            if result != exp:
                print("error")


