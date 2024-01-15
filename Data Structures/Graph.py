
class Node():
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def add_neighbour(self, node, cost):
        self.neighbours.append([node, cost])
        node.neighbours.append([self, cost])
        

class Graph():
    def __init__(self):
        pass
    
    def Depth_first_search(self, initial_node, goal_node):
        pass


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

node_1.add_neighbour(node_2, 2)
node_1.add_neighbour(node_3, 3)

node_2.add_neighbour(node_3, 3)
node_2.add_neighbour(node_5, 5)

node_3.add_neighbour(node_4, 4)

node_4.add_neighbour(node_5, 5)



"""
print(node_1.neighbours)
print(node_2.neighbours)
print(node_3.neighbours)
"""

graph_1 = Graph()
graph_1.Depth_first_search(node_1, node_5)