
def optional_character(c, str):
    if len(str) > 0 and (str[0] == c or c == "*"):
        str = str[1:]
    return str

def any_character(characters, str):
    result = ""
    new_res, str = optional_character(characters, str)
    result += new_res
    while new_res != "":
        new_res, str = optional_character(characters, str)
        result += new_res
    return (result, str)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        state = "start"
        if p == "" and s == "":
            return True
        if p == "":
            return False
        if p[0] == "*":
            return False

        previous_match
        current_match_letter = p[0]
        while s != "":
            if current_match_letter == ".":
                s = s[1:]
                curr



if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    assert s.largestRectangleArea([2, 1, 2]) == 3
    pass
