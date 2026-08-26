import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if groupSize > len(hand) or groupSize > (len(hand) // 2) + 1:
            return False
        heapq.heapify(hand)

        while hand:

            smallest = heapq.heappop(hand)
            for nxt in range(smallest+1, smallest + groupSize):# for next k elemnts not there or not
                if nxt not in hand : # curr + 1,+2 till k
                    return False
                hand.remove(nxt) # rm if all there

        return True







        