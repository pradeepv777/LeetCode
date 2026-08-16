class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        rev = ""
        for i in s:
            rev  = i + " " +rev
        return rev.rstrip()

        