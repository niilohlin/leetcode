
def optional_character(characters, str):
    result = ""
    if len(str) > 0 and str[0] in characters:
        result += str[0]
        str = str[1:]
    return (result, str)

def any_character(characters, str):
    result = ""
    new_res, str = optional_character(characters, str)
    result += new_res
    while new_res != "":
        new_res, str = optional_character(characters, str)
        result += new_res
    return (result, str)

class Solution:
    def myAtoi(self, s: str) -> int:
        _, s = any_character(" ", s)
        signChar, s = optional_character("+-", s)
        sign = {'+': 1, '-': -1}.get(signChar, 1)
        digits, _ = any_character("0123456789", s)
        if not digits:
            return 0
        return min(2**31-1, max(-2 ** 31, sign * int(digits)))




if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))