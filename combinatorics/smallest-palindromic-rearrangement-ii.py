import collections
import math

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1 

    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = collections.Counter(s)
        
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        half_counts = [0] * 26
        for char, count in counts.items():
            half_counts[ord(char) - ord('a')] = count // 2
            
        total_half_len = sum(half_counts)
        
        if self._countArrangements(half_counts) < k:
            return ""
            
        left_half = []
        for _ in range(total_half_len):
            for i in range(26):
                if half_counts[i] == 0:
                    continue
                
                half_counts[i] -= 1
                arrangements = self._countArrangements(half_counts)
                
                if arrangements >= k:
                    left_half.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    half_counts[i] += 1
                    
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]

    def _countArrangements(self, counts: list[int]) -> int:
        total = sum(counts)
        res = 1
        for freq in counts:
            if freq > 0:
                res *= self._nCk(total, freq)
                if res >= self.MAX:
                    return self.MAX
                total -= freq
        return res

    def _nCk(self, n: int, r: int) -> int:
        if r > n or r < 0:
            return 0
        if r == 0 or r == n:
            return 1
        if r > n - r:
            r = n - r
            
        res = 1
        for i in range(1, r + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX:
                return self.MAX
        return res
