from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = {}
        mid = ""

        for ch in sorted(cnt):
            half[ch] = cnt[ch] // 2
            if cnt[ch] % 2:
                mid = ch

        fact = [1]
        m = sum(half.values())
        for i in range(1, m + 1):
            fact.append(fact[-1] * i)

        def count_perm(freq):
            total = sum(freq.values())
            ans = fact[total]
            for v in freq.values():
                ans //= fact[v]
            return ans

        if count_perm(half) < k:
            return ""

        left = []

        while sum(half.values()) > 0:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count_perm(half)

                if ways >= k:
                    left.append(ch)
                    break

                k -= ways
                half[ch] += 1

        left = "".join(left)
        return left + mid + left[::-1]