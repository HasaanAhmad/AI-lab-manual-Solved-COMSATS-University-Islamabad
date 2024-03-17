import math

class Node:
    def __init__(self, state, actions=[]):
        self.state = state
        self.actions = actions
        self.parent = None
        self.totalCost = math.inf

graph = {
    'Arad': Node('Arad', [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)]),
    'Bucharest': Node('Bucharest', [('Giurgiu', 90), ('Pitesti', 101), ('Urziceni', 85)]),
    'Craiova': Node('Craiova', [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)]),
    'Drobeta': Node('Drobeta', [('Mehadia', 75)]),
    'Eforie': Node('Eforie'),
    'Fagaras': Node('Fagaras', [('Sibiu', 99), ('Bucharest', 211)]),
    'Giurgiu': Node('Giurgiu', [('Bucharest', 90)]),
    'Hirsova': Node('Hirsova', [('Urziceni', 98)]),
    'Iasi': Node('Iasi', [('Neamt', 87)]),
    'Lugoj': Node('Lugoj', [('Mehadia', 70)]),
    'Mehadia': Node('Mehadia', [('Lugoj', 70), ('Drobeta', 75)]),
    'Neamt': Node('Neamt', [('Iasi', 87)]),
    'Oradea': Node('Oradea', [('Zerind', 71)]),
    'Pitesti': Node('Pitesti', [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)]),
    'Rimnicu Vilcea': Node('Rimnicu Vilcea', [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)]),
    'Sibiu': Node('Sibiu', [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140), ('Oradea', 151)]),
    'Timisoara': Node('Timisoara', [('Arad', 118)]),
    'Urziceni': Node('Urziceni', [('Hirsova', 98), ('Bucharest', 85), ('Vaslui', 142)]),
    'Vaslui': Node('Vaslui', [('Urziceni', 142), ('Iasi', 92)]),
    'Zerind': Node('Zerind', [('Oradea', 71), ('Arad', 75)])
}

def findMin(frontier):
    minCost = math.inf
    minNode = None
    for node in frontier:
        if graph[node].totalCost < minCost:
            minCost = graph[node].totalCost
            minNode = node
    return minNode

def actionSequence(graph, initialstate, goalstate):
    solution = [goalstate]
    currentParent = graph[goalstate].parent
    while currentParent != initialstate:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.append(initialstate)
    solution.reverse()
    return solution

def UCS():
    initialstate = 'Arad'
    goalState = 'Bucharest'
    frontier = [initialstate]
    explored = []
    graph[initialstate].totalCost = 0

    while frontier:
        currentNode = findMin(frontier)
        frontier.remove(currentNode)
        explored.append(currentNode)

        if currentNode == goalState:
            return actionSequence(graph, initialstate, goalState)

        for child in graph[currentNode].actions:
            child_state, cost = child
            if child_state not in explored:
                if child_state not in frontier:
                    graph[child_state].parent = currentNode
                    graph[child_state].totalCost = graph[currentNode].totalCost + cost
                    frontier.append(child_state)
                elif graph[child_state].totalCost > graph[currentNode].totalCost + cost:
                    graph[child_state].parent = currentNode
                    graph[child_state].totalCost = graph[currentNode].totalCost + cost

solution = UCS()
print(solution)
