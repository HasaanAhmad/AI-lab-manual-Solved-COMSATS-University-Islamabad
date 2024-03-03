#SP22-BSE-017 HASAAN AHMAD 

import queue
maze = [
    ["#", "#", "#", "#", "#", "o", "#", "#"],
    ["#", "o", "o", "o", "o", "o", "o", "#"],
    ["#", "o", "#", "#", "#", "#", "o", "#"],
    ["#", "o", "#", "o", "#", "o", "o", "#"],
    ["#", "o", "#", "o", "#", "#", "o", "#"],
    ["#", "o", "#", "o", "#", "o", "o", "#"],
    ["#", "o", "o", "o", "o", "o", "o", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"],
]

start = (3, 3)  # Starting position
end = (0, 5)    # Destination position

queue = queue.Queue()
queue.put([start]) 
visited = set()
visited.add(start)

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  

while not queue.empty():
    current_path = queue.get()
    current_position = current_path[-1] 

    if current_position == end:
        print("Destination reached! Path:", current_path)
        break

    for direction in directions:
        new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

        if (
            0 <= new_position[0] < len(maze) and
            0 <= new_position[1] < len(maze[0]) and
            maze[new_position[0]][new_position[1]] != "#" and
            new_position not in visited
        ):
            new_path = list(current_path)
            new_path.append(new_position)
            queue.put(new_path)
            visited.add(new_position)



