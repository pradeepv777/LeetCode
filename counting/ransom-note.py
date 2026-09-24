class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            ransom_key = Counter(ransomNote)
            mag_key = Counter(magazine)

            # Returns true if every character count in ransomNote
            # is less than or equal to its count in magazine.
            return ransom_key <= mag_key
                