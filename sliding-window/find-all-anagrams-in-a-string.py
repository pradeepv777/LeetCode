class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        smap = Counter()
        pmap = Counter(p)
        res = []
        for i in range(len(s)):
            smap[s[i]]+=1

            if i >=len(p):
                left = s[i-len(p)]
                smap[left]-=1
                if smap[left]== 0:
                    del smap[left]
            if smap==pmap:
             res.append(i-len(p)+1)
        return res
        
                

        
        