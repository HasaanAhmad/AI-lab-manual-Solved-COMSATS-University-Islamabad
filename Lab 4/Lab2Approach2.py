board = [
    ['M','S','E','F'],
    ['R','A','T','D'],
    ['L','O','N','E'],
    ['K','A','F','B']
]
dictionary = ['START','NOTE','SAND','STONED']
def find_word(board, word,visited,x,y,result):
    if word in dictionary:
        result.add(word)
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    for direction in directions:
        dx,dy = direction
        if 0 <= x+dx < 4 and 0 <= y+dy < 4 and not visited[x+dx][y+dy]:
            visited[x+dx][y+dy] = True
            find_word(board,word+board[x+dx][y+dy],visited,x+dx,y+dy,result)
            visited[x+dx][y+dy] = False
    return result
def find_all_words(board):
    result = set()
    for i in range(4):
        for j in range(4):
            visited = [[False]*4 for _ in range(4)]
            visited[i][j] = True
            result = find_word(board,board[i][j],visited,i,j,result)
    return result
print(find_all_words(board))