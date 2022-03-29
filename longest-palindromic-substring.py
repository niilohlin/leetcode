
def is_palindrome(s):
    return s == "".join(list(reversed(s)))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = [[i] for i in range(len(s))] + [[i, i + 1] for i in range(len(s) - 1) if s[i] == s[i + 1]]

        longest_palindrome = []
        palindrome = palindromes.pop()
        while palindrome:
            if len(longest_palindrome) < len(palindrome):
                longest_palindrome = palindrome

            if palindrome[0] - 1 < 0 or palindrome[-1] + 1 >= len(s):
                if len(palindromes) > 0:
                    palindrome = palindromes.pop()
                    continue
                else:
                    break

            if s[palindrome[0] - 1] == s[palindrome[-1] + 1]:
                palindrome.insert(0, palindrome[0] - 1)
                palindrome.append(palindrome[-1] + 1)
                palindromes.append(palindrome)

            if len(palindromes) > 0:
                palindrome = palindromes.pop()
            else:
                break


        return "".join(list(map(lambda i: s[i], longest_palindrome)))

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("cbbd"))