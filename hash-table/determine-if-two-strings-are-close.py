class Solution:  
    """
    Since there are only 26 alphabets the total sorts can never go past
    26 sorts i.e(26 log(26)) = 122 operations which is the hard limit.
    """

    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_map = Counter(word1)
        word2_map = Counter(word2)
        
        if len(word2) != len(word1) :
            return False

        elif not sorted(word1_map.values()) == sorted(word2_map.values()):
            return False

        elif not sorted(word1_map.keys()) == sorted(word2_map.keys()):
            return False

        return True



    
        
        

        