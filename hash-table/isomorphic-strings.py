class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seenS = Counter(s)
        seenT = Counter(t)
        return list(seenS.values())== list(seenT.values())

        