# Generate a list of possible words from a character matrix
# Given an M × N boggle board, find a list of all possible words that can be formed by a sequence of 
# adjacent characters on the board.
# We are allowed to search a word in all eight possible directions, i.e., North, West, South, East, NorthEast, North-West, South-East, South-West, but a word should not have multiple instances of the same 
# cell.
# Consider the following the traditional 4 × 4 
# boggle board. If the input dictionary is [START, 
# NOTE, SAND, STONED], the valid words are 
# [NOTE, SAND, STONED].

# 4x4 Boggle Board
# M S E F
# R A T D
# L O N E
# S T O N


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

def findWords(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, trie.root, i, j, "", result)
    return list(result)

def dfs(board, node, i, j, path, result):
    if node.isEndOfWord:
        result.add(path)
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    temp = board[i][j]
    if temp not in node.children:
        return
    board[i][j] = "#"
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for direction in directions:
        x, y = i + direction[0], j + direction[1]
        dfs(board, node.children[temp], x, y, path + temp, result)
    board[i][j] = temp

board = [
    ["M", "S", "E", "F"],
    ["R", "A", "T", "D"],
    ["L", "O", "N", "E"],
    ["S", "T", "O", "N"]
]
words = ["START", "NOTE", "SAND", "STONED"]

print(findWords(board, words))
