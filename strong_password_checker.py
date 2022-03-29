from typing import List

def has_triplet(s):
    for i in range(len(s) - 3):
        if len(set(s[i:i+3])) == 1:
            return True
    return False

def has_lower(s):
    return any([c.islower() for c in s])

def has_upper(s):
    return any([c.isupper() for c in s])

def has_digit(s):
    return any([c.isdigit() for c in s])


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        changes_stack = [(0, password)]
        while changes_stack:
            (changes, suggested) = changes_stack.pop()

            if len(password) < 6:
                for c in "abcdefghijklmnopqrsteuvwxyzABCDEFGHIJKLMNOPQRSTEUVWXYZ01234567890":
                    changes_stack.append((changes + 1, c + suggested))
                continue
            if len(password) > 20:
                exit(1)
            if has_triplet(password):
                return
            if not has_lower(password):
                return
            if not has_upper(password):
                return
            if not has_digit(password):
                return
            break
        return changes


if __name__ == "__main__":
    s = Solution()
    print(s.strongPasswordChecker())
