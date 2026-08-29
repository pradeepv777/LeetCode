class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        curr_str = ""
        vowels = {"a", "e", "i", "o", "u"}
        counts = 0

        for char in s[:k]:
            curr_str += char
            if char in vowels:
                counts += 1
        max_vowels = counts

        if counts == k:
            return k

        for char in s[k:]:
            outgoing_char = curr_str[0]
            curr_str = curr_str[1:] + char

            if char in vowels:
                counts += 1

            if outgoing_char in vowels:
                counts -= 1
            max_vowels = max(max_vowels, counts)

        return max_vowels






        