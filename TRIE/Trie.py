class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
        
    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True
    
    
    def search(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endofword
    
    
    def startwith(self,prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            
        return True
    
    
trie = Trie()
a = "hello"
b = "hell"
c = "ello"
d = "llo"
trie.insert(a)
trie.insert(c)
trie.insert(d)
res = trie.search(b)
print("search result:",res)
result = trie.startwith(b)
print("search result:",result)

