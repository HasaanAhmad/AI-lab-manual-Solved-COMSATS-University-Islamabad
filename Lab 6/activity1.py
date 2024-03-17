import math
class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
    
graph = {
    'A' : Node('A', None, [('B',6), ('C',9), ('E',1)],0),
    'B' : Node('B', None, [('A',6), ('D',3), ('E',4)],0),
    'C' : Node('C', None, [('A',9), ('F',2), ('G',3),],0),
    'D' : Node('D', None, [('B',3), ('E',5),('F',7)],0),
    'E' : Node('E', None, [('A',1), ('B',4), ('D',5),('F',6)],0),
    'F' : Node('F', None, [('C',2), ('E',6), ('D',7)],0),
    'G' : Node('G', None, [('C',3)],0)
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
    initialstate = 'C'
    goalState = 'B'
    frontier = [initialstate]
    explored = []
    while frontier:
        currentNode = findMin(frontier)
        frontier.remove(currentNode)
        explored.append(currentNode)
        if currentNode == goalState:
            return actionSequence(graph, initialstate, goalState)
        for child in graph[currentNode].actions:
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = graph[currentNode].totalCost + child[1]
                frontier.append(child[0])
            elif child[0] in frontier:
                if graph[child[0]].totalCost > graph[currentNode].totalCost + child[1]:
                    graph[child[0]].parent = currentNode
                    graph[child[0]].totalCost = graph[currentNode].totalCost + child[1]

solution = UCS()
print(solution)
