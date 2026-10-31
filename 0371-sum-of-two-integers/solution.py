class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not a:
            return b
        if not b:
            return a

        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b & MASK:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        return a if a <= MAX_INT else ~ (a ^ MASK)

       