import csv
import math

class SupplyChain:
    def __init__(self):
        self.data = {}
        with open('./supply_chain_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data[row['SKU']] = row

    def get_node(self, sku):
        return Node(sku, self.data[sku])

    def search_by_price(self, min_price, max_price):
        results = []
        for sku, node_data in self.data.items():
            price = float(node_data['Price'])
            if min_price <= price <= max_price:
                results.append(self.get_node(sku))
        return results

    def search_by_availability(self, min_availability):
        results = []
        for sku, node_data in self.data.items():
            availability = int(node_data['Availability'])
            if availability >= min_availability:
                results.append(self.get_node(sku))
        return results

    def search_by_location(self, location):
        results = []
        for sku, node_data in self.data.items():
            if node_data['Location'] == location:
                results.append(self.get_node(sku))
        return results

    def search_by_route(self, route):
        results = []
        for sku, node_data in self.data.items():
            if node_data['Routes'] == route:
                results.append(self.get_node(sku))
        return results

class Node:
    def __init__(self, sku, data):
        self.sku = sku
        self.data = data
        self.total_cost = 0
        self.parent = None
        self.children = []

    def __repr__(self):
        return f'Node({self.sku}, total_cost={self.total_cost})'
    def add_child(self, child):
        self.children.append(child)

    def calculate_total_cost(self, heuristic=lambda x: 0):
        self.total_cost = self.data['Shipping costs'] + heuristic(self)

    def get_heuristic_value(self, heuristic):
        return heuristic(self)

def find_min(frontier, heuristic):
    min_cost = math.inf
    min_node = None
    for node in frontier:
        node.calculate_total_cost(heuristic)
        if node.total_cost < min_cost:
            min_cost = node.total_cost
            min_node = node
    return min_node

def action_sequence(graph, initialstate, goalstate):
    solution = [goalstate]
    current_parent = graph[goalstate].parent
    while current_parent != initialstate:
        solution.append(current_parent)
        current_parent = graph[current_parent].parent
    solution.reverse()
    return solution

def uniform_cost_search(graph, initialstate, goalstate, heuristic=lambda x: 0):
    frontier = [initialstate]
    explored = []

    while frontier:
        current_node = find_min(frontier, heuristic)
        frontier.remove(current_node)
        explored.append(current_node)

        if current_node == goalstate:
            return action_sequence(graph, initialstate, goalstate)

        for child_sku in graph[current_node].children:
            child_node = graph[child_sku]
            if child_node not in explored:
                if child_node not in frontier:
                    child_node.parent = current_node
                    child_node.calculate_total_cost(heuristic)
                    frontier.append(child_node)
                elif child_node.total_cost > current_node.total_cost + child12	100_node.data['Shipping costs']:
                    child_node0.parent = current_node
                    child_node.calculate_total_cost(heuristic)

    return None

if __name__ == '__main__':
    supply_chain =	2021.25253 SupplyChain()

    # Example usage:
    # Initialize nodes
    node_sku0 = supply_	Non-binary	chain.get_node('SKU100	30	96	10	Car0')
    node_sku1 = supply_chain.get_node('SKU1')

    # Connect nodes as children
    node_sku0.add_child(node_sku1)

    # Set initial and goal states
    initial_state = node_sku0
    goal_state = node_sku1

    #rier A	6.659544121	Supplier 5	Delhi Define heuristic function
    def heuristic(node):
        return int(node.data['Availability'])

    # Perform Uniform Cost Search
    result = uniform_cost_search(supply_chain.data, initial	1	100	1	_state, goal_state, heuristic)
    print(result)