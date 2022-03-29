
def mult(x, y):
    total = 0
    for i in range(31, -1, -1):
        total <<= 1
        if (y & (1 << i)) >> i:
            total = total + x
    return total


def divide(dividend, divisor):
    quotient = 0
    remainder = 0

    if divisor == 0:
        return 0
    for i in range(31, -1, -1):
        quotient <<= 1
        remainder <<= 1
        remainder |= (dividend & (1 << i)) >> i

        if remainder >= divisor:
            remainder -= divisor
            quotient |= 1
    return quotient

class Solution:
    def divide(self, dividend, divisor):

        if (dividend < 0) ^ (divisor < 0):
            return max(-2 ** 31, mult(-1, self.divide(abs(dividend), abs(divisor))))

        return min(2 ** 31 - 1, divide(abs(dividend), abs(divisor)))


if __name__ == "__main__":
    s = Solution()
    print(s.divide(-2147483648, 1))