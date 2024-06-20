class Node:
    def __init__(self):
        self.d = {}     # Dictionary to store child nodes
        self.flag = 0   # Flag to mark the end of a word

class Tries:
    def __init__(self):
        self.root = Node()  # Initialize the Trie with a root node
    
    def insert(self, word):
        t = self.root
        for char in word:
            if char not in t.d:
                t.d[char] = Node()  # Create a new node if the character doesn't exist
            t = t.d[char]
        t.flag = 1  # Mark the end of the word
    
    def search_word(self, word):
        t = self.root
        for char in word:
            if char not in t.d:
                return False
            t = t.d[char]
        return t.flag == 1  # Return True if it's a valid word
    
    def search_prefix(self, prefix):
        t = self.root
        for char in prefix:
            if char not in t.d:
                return False
            t = t.d[char]
        return True  # If we can traverse the Trie till the end of the prefix

    def _collect_words(self, node, prefix):
        words = []
        if node.flag == 1:
            words.append(prefix)  # Add the current prefix if it marks the end of a word
        for char, next_node in node.d.items():
            words.extend(self._collect_words(next_node, prefix + char))  # Recursively collect words
        return words
    
    def get_words_with_prefix(self, prefix):
        t = self.root
        for char in prefix:
            if char not in t.d:
                return []  # No words with the given prefix
            t = t.d[char]
        return self._collect_words(t, prefix)  # Start collecting words from the node corresponding to the prefix

# Example usage:
t1 = Tries()

# Insert words
t1.insert("school")
t1.insert("world")
t1.insert("word")
t1.insert("scholar")

# Search for words
print(t1.search_word("word"))  # True
print(t1.search_word("wood"))  # False

# Search for prefixes
print(t1.search_prefix("sch"))  # True
print(t1.search_prefix("wor"))  # True
print(t1.search_prefix("abc"))  # False

# Get words with a prefix
print(t1.get_words_with_prefix("sch"))  # ['school', 'scholar']
print(t1.get_words_with_prefix("wor"))  # ['world', 'word']
print(t1.get_words_with_prefix("abc"))  # []
