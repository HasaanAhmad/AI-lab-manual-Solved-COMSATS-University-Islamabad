import csv

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

data = {}
with open('./supply_chain_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data[row['SKU']] = row

root = Node(data['SKU0'])
for key, value in data.items():
    if key == 'SKU0':
        continue
    node = Node(value)
    root.add_child(node)

# Printing the tree


# Search Node Through SKU
def search_node(root):
    sku = input("Enter SKU: ")
    if sku not in data:
        print("Invalid SKU. Please try again.")
        return
    node = _search_node(root, sku)
    if node:
        print_node_info(node)
    else:
        print("Node not found.")

def _search_node(node, sku):
    if node.data['SKU'] == sku:
        return node
    for child in node.children:
        result = _search_node(child, sku)
        if result:
            return result
    return None

# Search using A* considering Availability being the heuristic
def search_node_a_star(root):
    sku = input("Enter SKU: ")
    if sku not in data:
        print("Invalid SKU. Please try again.")
        return
    open_list = [root]
    closed_list = []
    while open_list:
        current = min(open_list, key=lambda node: node.data['Availability'])
        open_list.remove(current)
        closed_list.append(current)
        if current.data['SKU'] == sku:
            print_node_info(current)
            return
        for child in current.children:
            if child not in closed_list:
                open_list.append(child)
    print("Node not found.")

# Search using BFS
def search_node_bfs(root):
    sku = input("Enter SKU: ")
    if sku not in data:
        print("Invalid SKU. Please try again.")
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.data['SKU'] == sku:
            print_node_info(current)
            return
        for child in current.children:
            queue.append(child)
    print("Node not found.")

# Search using DFS
def search_node_dfs(root):
    sku = input("Enter SKU: ")
    if sku not in data:
        print("Invalid SKU. Please try again.")
        return
    stack = [root]
    while stack:
        current = stack.pop()
        if current.data['SKU'] == sku:
            print_node_info(current)
            return
        for child in current.children:
            stack.append(child)
    print("Node not found.")

# Search using UCS considering Revenue generated being the cost also print costs being compared to show how its working
def search_node_ucs(root):
    sku = input("Enter SKU: ")
    if sku not in data:
        print("Invalid SKU. Please try again.")
        return
    queue = [(root, 0)]
    print("Costs being compared: ")
    while queue:
        current, cost = queue.pop(0)
        print(cost, current.data['Costs'])
        if current.data['SKU'] == sku:
            print_node_info(current)
            return
        for child in current.children:
            queue.append((child, cost + float(child.data['Costs'])))
    print("Node not found.")

# Search from one node to another node having heuristic as the cost
def search_path_cost(root):
    start_sku = input("Enter the starting SKU: ")
    end_sku = input("Enter the ending SKU: ")
    open_list = [root]
    closed_list = []
    while open_list:
        current = min(open_list, key=lambda node: node.data['Costs'])
        open_list.remove(current)
        closed_list.append(current)
        if current.data['SKU'] == end_sku:
            print_node_info(current)
            return
        for child in current.children:
            if child not in closed_list:
                open_list.append(child)
    print("Path not found.")

def print_node_info(node):
    print("-----------------------------------------")
    print("-----------------------------------------")
    print("\nSKU:", node.data['SKU'])
    print("Product Type:", node.data['Product type'])
    print("Price:", node.data['Price'])
    print("Availability:", node.data['Availability'])
    print("Available Stock:", node.data['Stock levels'])
    print("Quantity Available:", node.data['Order quantities'])
    print("\n-----------------------------------------")
    print("-----------------------------------------")

def menu():
    while True:
        print("--------------------------------------------------")
        print("--------------------------------------------------\n")
        print("SUPPLY CHAIN MANAGEMENT SYSTEM")
        print("1. Search Node Through SKU (e.g SKU2, SKU45 etc)")
        print("2. Search Node Through A*")
        print("3. Search Node Through BFS")
        print("4. Search Node Through DFS")
        print("5. Search Node Through UCS")
        print("6. Finding path from one node to another node heuristic as the cost")
        print("0. Exit\n")
        print("--------------------------------------------------")
        print("--------------------------------------------------\n")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                break
            elif choice == 1:
                search_node(root)
            elif choice == 2:
                search_node_a_star(root)
            elif choice == 3:
                search_node_bfs(root)
            elif choice == 4:
                search_node_dfs(root)
            elif choice == 5:
                search_node_ucs(root)
            elif choice == 6:
                search_path_cost(root)
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred: ", e)


if __name__ == '__main__':
    menu()
