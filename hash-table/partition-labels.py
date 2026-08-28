class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return [0]

        last_seen = {char: i for i, char in enumerate(s)}
        
        res = []
        left = 0  
        right = 0    
        
        for i, char in enumerate(s):
            right = max(right, last_seen[char])
            
            if i == right:
                res.append(right - left + 1)
                left = i + 1  

        return res
