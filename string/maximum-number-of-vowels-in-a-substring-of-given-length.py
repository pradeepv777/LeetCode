class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s:
            return 0

        vowels = {"a", "e", "i", "o", "u"}
        count = 0

        # Count vowels in the first window size k
        for char in s[:k]:
            if char in vowels:
                count += 1
        max_count = count

        if count == k:
            return k
        # Slide the window using direct index lookups
        for r in range(k, len(s)):
            if s[r] in vowels:
                count += 1

            # Remove chars on the left(at index r - k)
            if s[r - k] in vowels:
                count -= 1
            max_count = max(max_count, count)

        return max_count
