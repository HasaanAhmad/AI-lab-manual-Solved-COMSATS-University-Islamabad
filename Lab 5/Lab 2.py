# Generate a list of possible words from a character matrix
# Given a 8 × 8 boggle board, find a list of all possible words that can 
# be formed by a sequence of adjacent characters on the board.
# We are allowed to search a word in all eight possible directions, i.e., 
# North, West, South, East, North-East, North-West, South-East, 
# South-West, but a word should not have multiple instances of the 
# same cell.
# Consider the following the traditional 4 × 4 boggle board. If the 
# input dictionary is [START, NOTE, SAND, STONED], the valid 
# words are [NOTE, SAND, STONED]. With iterative deepening, create words of length 5, 6, 7 and 8 
# through each iteration

#SP22-BSE-017 HASAAN AHMAD


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def remove(self, word):
        def helper(node, word, index):
            if index == len(word):
                if not node.isEndOfWord:
                    return False
                node.isEndOfWord = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            shouldDeleteCurrentNode = helper(node.children[char], word, index + 1)
            if shouldDeleteCurrentNode:
                del node.children[char]
                return len(node.children) == 0
            return False
        helper(self.root, word, 0)

def isSafe(i, j, visited):
    return i >= 0 and i < 4 and j >= 0 and j < 4 and not visited[i][j]

def searchWord(boggle, i, j, visited, trieNode, str):
    if trieNode.isEndOfWord:
        print(str)
    
    if isSafe(i, j, visited):
        visited[i][j] = True
        for k in range(26):
            if trieNode.children.get(chr(k + ord('A'))):
                ch = chr(k + ord('A'))
                if i - 1 >= 0 and j - 1 >= 0 and boggle[i - 1][j - 1] == ch:
                    searchWord(boggle, i - 1, j - 1, visited, trieNode.children[ch], str + ch)
                if i - 1 >= 0 and boggle[i - 1][j] == ch:
                    searchWord(boggle, i - 1, j, visited, trieNode.children[ch], str + ch)
                if i - 1 >= 0 and j + 1 < 4 and boggle[i - 1][j + 1] == ch:
                    searchWord(boggle, i - 1, j + 1, visited, trieNode.children[ch], str + ch)
                if j - 1 >= 0 and boggle[i][j - 1] == ch:
                    searchWord(boggle, i, j - 1, visited, trieNode.children[ch], str + ch)
                if j + 1 < 4 and boggle[i][j + 1] == ch:
                    searchWord(boggle, i, j + 1, visited, trieNode.children[ch], str + ch)
                if i + 1 < 4 and j - 1 >= 0 and boggle[i + 1][j - 1] == ch:
                    searchWord(boggle, i + 1, j - 1, visited, trieNode.children[ch], str + ch)
                if i + 1 < 4 and boggle[i + 1][j] == ch:
                    searchWord(boggle, i + 1, j, visited, trieNode.children[ch], str + ch)
                if i + 1 < 4 and j + 1 < 4 and boggle[i + 1][j + 1] == ch:
                    searchWord(boggle, i + 1, j + 1, visited, trieNode.children[ch], str + ch)
        visited[i][j] = False

def findWords(boggle, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    visited = [[False for _ in range(4)] for _ in range(4)]
    trieNode = trie.root
    str = ""
    for i in range(4):
        for j in range(4):
            if trieNode.children.get(boggle[i][j]):
                str = str + boggle[i][j]
                searchWord(boggle, i, j, visited, trieNode.children[boggle[i][j]], str)
                str = ""
    return

board = [
    ["M", "S", "E", "F"],
    ["R", "A", "T", "D"],
    ["L", "O", "N", "E"],
    ["S", "T", "O", "N"]
]

words = ["START", "NOTE", "SAND", "STONED"]

findWords(board, words)

