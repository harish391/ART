class ARTNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class AdaptiveRadixTree:
    def __init__(self):
        self.root = ARTNode()

    def insert(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = ARTNode()
            node = node.children[char]
        node.is_end = True

    def search(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
