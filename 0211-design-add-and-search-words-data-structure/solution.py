class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        curr  = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["/"] = "/"

    def search(self, word: str) -> bool:
        def dfs(curr, idx):
            if idx == len(word):
                return bool("/" in curr)
            letter = word[idx]

            if letter != '.':
                if letter not in curr:
                    return False
                else:
                    return dfs(curr[letter], idx+1)
            else:
                return any(dfs(curr[letter], idx + 1) for letter in curr if letter != "/")
        return dfs(self.trie, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)