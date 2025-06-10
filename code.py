class TrieNode:
    def _init_(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def _init_(self):
        """
        Initializes the trie object.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie (i.e., was inserted before),
        and false otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the prefix prefix,
        and false otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# --- Example Usage (from your problem description) ---
# Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output: [null, null, true, false, true, null, true]

if __name__ == "_main_":
    results = []
    trie = None # Initialize trie outside the loop

    actions = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    parameters = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    for i in range(len(actions)):
        action = actions[i]
        params = parameters[i]

        if action == "Trie":
            trie = Trie()
            results.append(None)
        elif action == "insert":
            word = params[0]
            trie.insert(word)
            results.append(None)
        elif action == "search":
            word = params[0]
            results.append(trie.search(word))
        elif action == "startsWith":
            prefix = params[0]
            results.append(trie.startsWith(prefix))
    
    print(results)
