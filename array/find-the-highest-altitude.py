class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] * len(gain)
        res[0] = gain[0] # [-5,0,0,0,0]

        for i in range(1, len(gain)):
            res[i] = res[i-1] + gain[i]

        return max(0,max(res))

        