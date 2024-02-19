graph = {
    'Arad': [('Timisoara', 75), ('Sibiu', 140)],
    'Timisoara': [('Arad', 75), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 120)],
    'Drobeta': [('Mehadia', 120), ('Craiova', 151)],
    'Craiova': [('Drobeta', 151), ('Pitesti', 101), ('Rimnicu Vilcea', 138)],
    'Pitesti': [('Craiova', 101), ('Rimnicu Vilcea', 97), ('Bucharest', 101)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Sibiu', 80), ('Fagaras', 146)],
    'Sibiu': [('Arad', 140), ('Rimnicu Vilcea', 80), ('Fagaras', 99)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Bucharest': [('Fagaras', 211), ('Urziceni', 85), ('Giurgiu', 87)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Giurgiu': [('Bucharest', 87)],
    'Iasi': [('Neamt', 85), ('Urziceni', 92)],
    'Neamt': [('Iasi', 92)],
    'Oradea': [('Zerind', 111), ('Sibiu', 151)]
}

import collections

def bfs(graph, start, end):
    queue = collections.deque([(start, [start])])
    
    while queue: 
        (node, path) = queue.popleft()
        
        if node == end:
            return path
            
        for (neighbor, distance) in graph[node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
            
    return None

path = bfs(graph, 'Arad', 'Bucharest')
print(path)

