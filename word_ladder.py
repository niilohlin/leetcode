from typing import List


from collections import defaultdict, Counter
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList += [beginWord]

        graph = defaultdict(set)
        for word in wordList:
            graph[word] = set()

        for word in wordList:
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    chars = list(word)
                    chars[i] = c
                    new_word = "".join(chars)
                    if new_word in graph and new_word != word:
                        graph[word].add(new_word)

        paths = [[beginWord]]
        all_visited_nodes = set()
        while len(paths) != 0:
            path = paths.pop()
            current_word = path[-1]
            if current_word == endWord:
                return len(path)
            for neighbour in graph[current_word]:
                if neighbour in all_visited_nodes:
                    continue
                paths.insert(0, path + [neighbour])
                all_visited_nodes.add(neighbour)

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
