class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        left = 1
        right = max_pile
        min_vals = []

        while left<=right:
            k = (left+right)//2
            total_hrs = 0

            for i in piles:
                total_hrs+= i//k
                if i % k != 0 :
                    total_hrs+=1

            if total_hrs <= h:
                min_vals.append(k)
                right = k-1
            else:
                left = k+1

            if total_hrs> h:
                left = k+1
            else:
                right = k-1
        return min(min_vals)
            



        