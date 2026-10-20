from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = Counter(nums)
        sorte = sorted(seen.keys(), key = lambda x: seen[x], reverse = True)
        return sorte[:k]

        

            

