import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if groupSize > len(hand):
            return False

        hand_map = Counter(hand)
        heapq.heapify(hand)

        while hand:

            smallest = heapq.heappop(hand)
            if hand_map[smallest] == 0:
                continue

            for nxt in range(smallest, smallest + groupSize):

                if hand_map[nxt] <= 0:
                    return False
                
                hand_map[nxt] -= 1

        return True


  
            
