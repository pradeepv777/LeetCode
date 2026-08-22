class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        i = 0

        while i <= n:
            count = 0
            num = i

            while num > 0:
                rem = num % 2
                num = num // 2
                if rem == 1:
                    count+= 1

            res.append(count)
            i+=1

        return res
        