class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        dictionary = self.trie

        for c in word:
            if c not in dictionary:
                dictionary[c] = {} # create empty dict when new char appears
            dictionary = dictionary[c]

        dictionary["."] = "."
        
    def search(self, word: str) -> bool:
        dictionary = self.trie

        for c in word:
            if c not in dictionary:
                return False
            dictionary = dictionary[c]

        return '.' in dictionary

    def startsWith(self, prefix: str) -> bool:
        dictionary = self.trie
        for c in prefix:
            if c not in dictionary:
                return False

            dictionary = dictionary[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)