class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        maps = {}
        
        for i in strs:
            sorted_key = "".join(sorted(i))
            if sorted_key not in maps:
                maps[sorted_key] = []
            maps[sorted_key].append(i)

        return list(maps.values())

        