from typing import List

from collections import defaultdict
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = defaultdict(lambda: 0)

        for i, x in enumerate(reversed(num1)):
            for j, y in enumerate(reversed(num2)):
                intermediate_result = int(x) * int(y)
                for remainder_index, r in enumerate(reversed(str(intermediate_result))):
                    result[i + j + remainder_index] += int(r)
                print("intermediate")


        resulting_string = ""
        for key in reversed(sorted(result.keys())):
            resulting_string += str(result[key])
        return resulting_string




if __name__ == "__main__":
    s = Solution()
    print(s.multiply("129", "2"))
    print(s.multiply("123", "456"))
