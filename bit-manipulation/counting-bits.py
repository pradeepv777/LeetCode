class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        i = 0
        count = 0
        while i <= n:
            rem = i % 2
            i = i // 2
            if rem == 1:
                count+= 1

            res.append(count)
        count = 0
        i+=1

        return res
        