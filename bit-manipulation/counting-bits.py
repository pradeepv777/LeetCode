class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1) # 0 -> n

        for i in range(1,n+1):

            res[i] = (i % 2) + res[i // 2]
        return res
        