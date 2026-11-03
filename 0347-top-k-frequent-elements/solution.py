class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        sorte = sorted(count.items(), key = lambda x : x[1], reverse = True)
        return [i[0] for i in sorte[:k]]

        