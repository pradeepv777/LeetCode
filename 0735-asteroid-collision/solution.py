class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []

        for i in asteroids: # while +ve asteroid and next one is -ve
            while res and i < 0 < res[-1]:
                if abs(i) > res[-1]: # if value at (-i) is grrater than res number
                    res.pop()
                    continue
                elif abs(i) == res[-1]: # Incase equal pop both
                    res.pop()
                break
            else: # if not -ve num append to result stack
                res.append(i)
        return res


        