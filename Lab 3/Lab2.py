maze = [
    ['S', '.', '.', '.', '.'],
    ['.', '.', '.', 'B', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'E']
]

def bfs(maze, start):
    # Define the possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Create a queue and add the start node to it
    queue = [(start, [start])]

    # Loop until the queue is empty
    while queue:
        # Get the next node to visit from the queue
        node, path = queue.pop(0)

        # If we have reached the end, return the path
        if maze[node[0]][node[1]] == 'E':
            return path

        # Otherwise, try to move in each of the four possible directions
        for move in moves:
            x, y = node[0] + move[0], node[1] + move[1]

            # Check if the move is valid (i.e., within the maze and not a wall)
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                # If we haven't visited this node before, add it to the queue
                if (x, y) not in path:
                    queue.append(((x, y), path + [(x, y)]))

    # If we haven't found a path, return None
    return None

# Find the path through the maze using BFS
path = bfs(maze, (0, 0))

# Print the path
if path:
    for node in path:
        print(node)
else:
    print("No path found!")