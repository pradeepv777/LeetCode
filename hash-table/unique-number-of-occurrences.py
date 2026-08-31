class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        arr_map = Counter(arr)
        return len(arr_map.values()) == len(set(arr_map.values()))

        



        
        