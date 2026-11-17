class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        res = []

        for spell in spells:
            left = 0
            right = len(potions) - 1
            i = len(potions) 

            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    i = mid
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(len(potions) - i)
        return res











        


        