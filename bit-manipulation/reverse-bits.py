class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""

        while n > 0:
            binary = str(n % 2) + binary
            n = n // 2

        return int(binary)
        