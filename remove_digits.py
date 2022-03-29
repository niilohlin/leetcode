from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        smallest = int(num)
        for _ in range(k):
            num_copy = num
            for i in range(len(num_copy)):
                try:
                    if int(num_copy[:i] + num_copy[i + 1:]) < smallest:
                        smallest = int(num_copy[:i] + num_copy[i + 1:])
                        num = num_copy[:i] + num_copy[i + 1:]
                except ValueError:
                    return "0"
        return str(smallest)



if __name__ == "__main__":
    s = Solution()
    print(s.removeKdigits("10", 2))
