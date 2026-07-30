from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       s1map = Counter(s1)
       s2map = Counter()

       for i in range(len(s2)):
          s2map[s2[i]] +=1
          if i>= len(s1):
            left = s2[i -len(s1)]
            s2map[left]-=1
            if s2map[left] == 0:
                del s2map[left]
          if s1map == s2map:
            return True
       return False



            

            

        