def iterative_deepening_dfs(dic_graph, target):
    depth = 1
    bottom_reached = False
    while not bottom_reached:
        result, bottom_reached = iterative_deepening_dfs_rec(dic_graph, target, 0, depth)
        if result is not None:
            return result
        depth *= 2
        print("Increasing depth to "+ str(depth))
    return None

def iterative_deepening_dfs_rec(node, target, current_depth, max_depth):
    print("Visiting Node " + str(node["value"]))
    if node["value"] == target:
        print("Found the node !")
        return node, True
    if current_depth == max_depth:
        print("Current maximum depth reached, returning...")
        if len(node["children"]) > 0:
            return None, False
        else:
            return None, True
        
    bottom_reached = True
    for i in range(len(node["children"])):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(node["children"][i], target, current_depth + 1, max_depth)
        if result is not None:
            return result, True
        bottom_reached = bottom_reached and bottom_reached_rec
    return None, bottom_reached

dictionary = {
    "value": "Arad",
    "children": [
        {"value": "Sibiu",
         "children": [
             {"value": "Fagaras", "children": []},
             {"value": "Rimnicu", "children": []}
         ]},
        {"value": "Zerind",
         "children": [
             {"value": "Oradea", "children": []}
         ]},
        {"value": "Timisoara",
         "children": [
             {"value": "Lugoj", "children": []}
         ]},
        {"value": "Oradea", "children": []},
        {"value": "Rimnicu",
         "children": [
             {"value": "Pitesti", "children": []},
             {"value": "Craiova", "children": []}
         ]},
        {"value": "Fagaras",
         "children": [
             {"value": "Bucharest", "children": []}
         ]},
        {"value": "Craiova",
         "children": [
             {"value": "Pitesti", "children": []}
         ]},
        {"value": "Pitesti",
         "children": [
             {"value": "Bucharest", "children": []}
         ]},
        {"value": "Bucharest",
         "children": [
             {"value": "Giurgiu", "children": []},
             {"value": "Urziceni", "children": []}
         ]},
        {"value": "Urziceni",
         "children": [
             {"value": "Hirsova", "children": []},
             {"value": "Vaslui", "children": []}
         ]},
        {"value": "Hirsova",
         "children": [
             {"value": "Eforie", "children": []}
         ]},
        {"value": "Eforie", "children": []},
        {"value": "Iasi",
         "children": [
             {"value": "Neamt", "children": []}
         ]},
        {"value": "Neamt", "children": []},
        {"value": "Vaslui", "children": []},
        {"value": "Giurgiu", "children": []}
    ]
}

try:
    print(iterative_deepening_dfs(dictionary, "Bucharest")["value"])
except:
    print("Node not found in Graph.")