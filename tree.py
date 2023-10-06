class Node:
    #The idea is that the node stores a board state.
    def __init__(self, _value, _path_cost, _parent_node, f = None):
        self.value = _value
        self.path_cost = _path_cost
        self.children = []
        self.f = f
        self.parent_node = _parent_node
    
    def add_child (self, new_child, _path_cost):
        self.children.append(Node(new_child, _path_cost, self))

    def set_f (self, f_value):
        self.f = f_value

class Tree:
    def __init__(self, _root_value, _path_cost, f = None):
        self.root = Node(_root_value, _path_cost, None, f)

    def add_child_to (self, parent_node, value):
        parent_node.add_child(value)

