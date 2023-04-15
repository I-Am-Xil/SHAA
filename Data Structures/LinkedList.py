

class Node():
    def __init__(self, value):        
        self.value = value
        self.next_node = None


class Linked_List():
    def __init__(self, head_node):
        self.head = head_node
        
    
    def print(self):
        node = self.head
        print(node.value)
        
        while node.next_node:
            node = node.next_node
            print(node.value)
        return 1
            
    
    def search(self, objective_node):
        node = self.head
        
        while node is not objective_node:
            try:
                node = node.next_node
            except:
                print("No match found")
                return -1
        return node
    
    
    #* Searches for the first node with @value = value
    def search_value(self, value):
        node = self.head
        
        while node.value != value:
            try:
                node = node.next_node
            except:
                print("No match found")
                return -1
        return node
    

    def search_parent(self, child_node):
        parent = self.head
        
        while parent.next_node is not child_node:
            try:
                parent = parent.next_node
            except:
                print("No match found")
                return -1
        return parent
    
    
    def append(self, child_node):
        parent = self.head
        
        while parent.next_node:
            parent = parent.next_node
        
        parent.next_node = child_node
        return 1
        
        
    def insert(self, parent_node, child_node):
        parent = self.search(parent_node)
        
        try:
            child_node.next_node = parent_node.next_node
        except:
            pass
        
        parent.next_node = child_node
        return 1
        
        
    def insert_head(self, new_head):
        new_head.next_node = self.head
        self.head = new_head
        return 1
        
    
    def pop(self, popped_node):
        parent = self.search_parent(popped_node)
        
        parent.next_node = popped_node.next_node
        popped_node.next_node = Node(None)
        return 1
        
    
    def pop_head(self):
        ex_head = self.head
        
        try:
            self.head = self.head.next_node
        except:
            print("Non iterable linked list")
            return -1
        
        ex_head.next_node = Node(None)
        return 1
        
    
    #* Deletes the first node with @value = value
    def delete(self, value):
        to_be_deleted = self.search_value(value)
        
        if to_be_deleted == self.head:
            self.pop_head()
            return 1
        
        try:
            parent = self.search_parent(to_be_deleted)
        except:
            print("No match found")
            return -1
            
        new_child = to_be_deleted.next_node
        parent.next_node = new_child
        
        return 1
        
    
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node2_2 = Node(2)


node1.next_node = node2
node2.next_node = node3
node3.next_node = node2_2


#* Tests
lkd_list = Linked_List(node1)
lkd_list.print()
print("\n")

lkd_list.append(node4)
lkd_list.print()
print("\n")

lkd_list.insert(node3, node5)
lkd_list.print()
print("\n")

lkd_list.insert_head(node6)
lkd_list.print()
print("\n")

lkd_list.pop(node1)
lkd_list.print()
print("\n")

lkd_list.pop_head()
lkd_list.print()
print("\n")

lkd_list.delete(3)
lkd_list.print()
print("\n")

#* Try deleting head value
lkd_list.delete(2)
lkd_list.print()
print("\n")