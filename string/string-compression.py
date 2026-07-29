class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = []
        i = 0
        n = len(chars)
        while i < n:
            count = 1

            while i + 1 < n and chars[i] == chars[i + 1]:
                count += 1
                i += 1

            compressed.append(chars[i])
            if count > 1:
                compressed.extend(str(count))
            i += 1
        chars[:] = compressed
        return len(chars)