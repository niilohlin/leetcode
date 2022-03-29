#/usr/bin/env python

from typing import Dict


class WordDictionary:

    def __init__(self):
        self.subDicts = dict()
        self.debugWords = []
        pass

    def addWord(self, word: str) -> None:
        self.debugWords.append(word)
        if len(word) == 0:
            self.subDicts[""] = WordDictionary()
            return

        subDict = WordDictionary()
        if word[0] in self.subDicts.keys():
            subDict = self.subDicts[word[0]]
        subDict.addWord(word[1:])

        self.subDicts[word[0]] = subDict

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return word in self.subDicts.keys()
        if word[0] == ".":
            return any([self.subDicts[key].search(word[1:]) for key in self.subDicts.keys() if key != ""])

        return word[0] in self.subDicts.keys() and self.subDicts[word[0]].search(word[1:])


def flat_map(f, iterable):
    return [subX for x in iterable for subX in f(x)]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

def assertEquals(a, b, comment):
    if a == b:
        return
    print(f"{a} not equal {b}, {comment}")

def run(list, args, expected):
    wd = WordDictionary()

    for f, arg, e in zip(list, args, expected):
        if f == "WordDictionary":
            wd = WordDictionary()
            assert e == None
        elif f == "addWord":
            print("adding word: " + arg[0])
            wd.addWord(arg[0])
            assert e == None
        elif f == "search":
            assertEquals(wd.search(arg[0]), e, f"searched {arg[0]} in db: {wd.debugWords}")


if __name__ == "__main__":

    actions = ["WordDictionary","addWord","addWord","search","search","search","search","search","search","search","search"]
    args = [[],["a"],["ab"],["a"],["a."],["ab"],[".a"],[".b"],["ab."],["."],[".."]]

    expected = [None,None,None,True,True,True,False,True,False,True,True]

    run(actions, args, expected)


