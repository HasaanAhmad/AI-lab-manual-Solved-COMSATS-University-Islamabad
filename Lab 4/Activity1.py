class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
    
graph = {
    'A': Node('A', None, ['B','E','C'],None),
    'B': Node('B', None, ['D','E','A'],None),
    'C': Node('C', None, ['A','F','G'],None),
    'D': Node('D', None, ['B','E'],None),
    'E': Node('E', None, ['A','B','D'],None),
    'F': Node('F', None, ['C'],None),
    'G': Node('G', None, ['C'],None)
}
def DFS():
    frontier = ['D']
    explored = []
    goalstate = 'C'
    while frontier:
        currentNode = frontier.pop()
        print(currentNode)
        explored.append(currentNode)
        if currentNode == goalstate:
            return actionSequence(graph, 'D', 'C')
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                frontier.append(child)
                
def actionSequence(graph, initialstate, goalstate):
    solution = [goalstate]
    currentParent = graph[goalstate].parent
    while currentParent != initialstate:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.append(initialstate)
    solution.reverse()
    return solution

solution = DFS()
print(solution)