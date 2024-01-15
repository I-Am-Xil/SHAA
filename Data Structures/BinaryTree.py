

#* i was trying to do depth first search, but ended up reinventing breath first search


class Node():
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None


class BinaryTree():
    def __init__(self, head):
        self.head = head


    def Breath_first_search_traversal(self, objective_node):
        visited = []
        found_not_visited = [self.head]
        
        steps = 0
        
        while found_not_visited or (objective_node in visited):
            
            steps += 1
            
            #* Using 0 because we are using the list as a queue
                        
            node = found_not_visited[0]
            
            if node not in visited:
                visited.append(node)
                found_not_visited.pop(0)
                
            if objective_node in visited:
                break

            if node.left_node:
                if node.left_node not in visited:
                    found_not_visited.append(node.left_node)
                    
            if node.right_node:
                if node.right_node not in visited:
                    found_not_visited.append(node.right_node)
        
        if objective_node not in visited:
            print("Error code 1. Object not found")
            return 1
        
        print("Steps: ", steps)
        return visited
    
    
    def Depth_first_search_traversal(self, objective_node):
        visited = []
        found_not_visited = [self.head]
        
        steps = 0
        
        while found_not_visited or (objective_node in visited):
            
            steps += 1
            
            #* Using 0 because we are using the list as a stack
                        
            node = found_not_visited[0]
            
            if node not in visited:
                visited.append(node)
                found_not_visited.pop(0)
                
            if objective_node in visited:
                break

            if node.right_node:
                if node.right_node not in visited:
                    found_not_visited.insert(0, node.right_node)

            if node.left_node:
                if node.left_node not in visited:
                    found_not_visited.insert(0, node.left_node)
        
        if objective_node not in visited:
            print("Error code 1. Object not found")
            return 1
        
        print("Steps: ", steps)
        return visited
        
    
    def Depth_first_search_traversal_recursive(self, objective_node, head_node = None):
        visited = []
        left_subtree = []
        right_subtree = []
        
        node = head_node
        
        if node == None:
            node = self.head
            
        visited.append(node)
        
        if objective_node in visited:
            return visited
            
        if node.left_node:
            
            if objective_node in visited:
                return visited
        
            left_subtree = self.Depth_first_search_traversal_recursive(objective_node, node.left_node)
            visited.extend(left_subtree)
                
        if node.right_node:
            
            if objective_node in visited:
                return visited
            
            right_subtree = self.Depth_first_search_traversal_recursive(objective_node, node.right_node)
            visited.extend(right_subtree)
            
        return visited
    
    
    def ToBeDecided():
        pass
            
        
    
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

node1.left_node = node2
node1.right_node = node3

node2.left_node = node4
node2.right_node = node5

node3.left_node = node6
node3.right_node = node7

node4.left_node = node8

my_tree = BinaryTree(node1)

print("Recursive depth first search")
search = my_tree.Depth_first_search_traversal_recursive(node7)
for i in search:
    print(i.value)

print("Depth first search")
search = my_tree.Depth_first_search_traversal(node7)
for i in search:
    print(i.value)

print("\nBreath first search")
search = my_tree.Breath_first_search_traversal(node7)
for i in search:
    print(i.value)

