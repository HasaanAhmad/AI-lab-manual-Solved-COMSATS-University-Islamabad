dictionary = ["START","NOTE", "SAND", 'STONED']
n = len(dictionary)
M = 4
N = 4

def isWord(Str):
    for i in range(n):
        if (Str == dictionary[i]):
            return True
    return False

def findWordsUtil(boggle, visited, i, j, Str, depth):
    if isWord(Str):
        print(Str)

    if depth <= 0:
        return

    row = i - 1
    while row <= i + 1 and row < M:
        col = j - 1
        while col <= j + 1 and col < N:
            if row >= 0 and col >= 0 and not visited[row][col]:
                findWordsUtil(boggle, visited, row, col, Str + boggle[row][col], depth - 1)
            col += 1
        row += 1

    visited[i][j] = False


def findWords(boggle):
    visited = [[False for _ in range(N)] for _ in range(M)]

    for depth in range(1, max(M, N) + 1):
        for i in range(M):
            for j in range(N):
                findWordsUtil(boggle, visited, i, j, boggle[i][j], depth)


boggle = [
    ["M", "S", "E", "F"],
    ["R", "A", "T", "D"],
    ["L", "O", "N", "E"],
    ["K", "A", "F", "B"]
]

print("Following words of", "dictionary are present:")
findWords(boggle)