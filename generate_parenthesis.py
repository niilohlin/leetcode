from typing import List

def flat_map(f, iterable):
    return [subX for x in iterable for subX in f(x)]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = {"()"}
        for i in range(1, n):
            sub_result = set()
            for exp in result:
                for char_index in range(len(exp)):
                    new = exp[:char_index] + "()" + exp[char_index:]
                    sub_result.add(new)
            result = (sub_result)
        return list(result)



if __name__ == "__main__":
    s = Solution()
    print(list(reversed(s.generateParenthesis(3))))
