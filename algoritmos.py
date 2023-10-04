import tree
import tabuleiro

def generate_children (node):
    parent_nodes = []
    parent_nodes.append(node)
    if node.parent_node is not None:
        parent_nodes.append(node.parent_node)
    current = node.parent_node
    while (current is not None):
        parent_nodes.append(current)
        current = current.parent_node
    
    zero_idx = node.value.find_zero()
    if node.value.check_move_up(zero_idx[0], zero_idx[1]):
        new_board = node.value.move_up(zero_idx[0], zero_idx[1])
        count = 0
        #used to cut nodes that have been explored
        for parent in parent_nodes:
            if not (parent.value.compare_boards(new_board)):
                count += 1
        if count == len (parent_nodes):
            node.add_child(new_board, node.path_cost+1)
    if node.value.check_move_down(zero_idx[0], zero_idx[1]):
        new_board = node.value.move_down(zero_idx[0], zero_idx[1])
        count = 0
        for parent in parent_nodes:
            if not (parent.value.compare_boards(new_board)):
                count += 1
        
        if count == len (parent_nodes):
            node.add_child(new_board, node.path_cost+1)
    if node.value.check_move_left(zero_idx[0], zero_idx[1]):
        new_board = node.value.move_left(zero_idx[0], zero_idx[1])
        count = 0
        for parent in parent_nodes:
            if not (parent.value.compare_boards(new_board)):
                count += 1
        
        if count == len (parent_nodes):
            node.add_child(new_board, node.path_cost+1)
    if node.value.check_move_right(zero_idx[0], zero_idx[1]):
        new_board = node.value.move_right(zero_idx[0], zero_idx[1])
        count = 0
        for parent in parent_nodes:
            if not (parent.value.compare_boards(new_board)):
                count += 1
        
        if count == len (parent_nodes):
            node.add_child(new_board, node.path_cost+1)

def search_explored (state, explored):
    num_entries = len(state) * len(state[0])
    for explored_state in explored:
        count = 0
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == explored_state[i][j]:
                    count += 1
        
        if count == num_entries:
            return True
    
    return False


def BFS (board, solution):
    tree_1 = tree.Tree(board, 0)

    if solution.compare_boards(tree_1.root.value):
        return (tree_1.root)
    else:
        frontier = [tree_1.root]
        explored = []
        while(len(frontier) > 0):
            exploring = frontier.pop(0)
            explored.append(exploring.value.board)
            generate_children(exploring)
            
            for child in exploring.children:
                if (child not in frontier or search_explored(child.value.board, explored)):
                    if solution.compare_boards(child.value):
                        return (child)
                    else:
                        frontier.append(child)
    

def IDS (board, solution):
    limit = 0
    tree_1 = tree.Tree(board, 0)

    while True:
        result = DFS(tree_1.root, solution, limit)

        if type(result) is not str:
            return result
        elif result == "cutoff":
            limit += 1
        elif result == "failure":
            return None

def DFS (node, solution, limit):
    if solution.compare_boards(node.value):
        return (node)
    if limit == 0:
        return ("cutoff")
    
    cutoff_occured = False
    generate_children(node)
    
    for child in node.children:
        result = DFS(child, solution, limit-1)
        if type(result) is not str:
            return result
        elif result == "cutoff":
            cutoff_occured = True
        
    if cutoff_occured:
        return "cutoff"
    else:
        return "failure"

def check_frontier (frontier, value_1):
    for item in frontier:
        if item.value.compare_boards(value_1):
            return True
    return False
    
def UCS (board, solution):
    tree_1 = tree.Tree(board,0)
    frontier = [tree_1.root]
    explored = set()

    while(len(frontier) > 0):
        exploring = frontier.pop(0)
        if solution.compare_boards(exploring.value):
            return (exploring)
        explored.add(exploring.value)
        generate_children(exploring)

        for child in exploring.children:
            if child.value not in explored or child not in frontier:
                frontier.append(child)
            else:
                for i, item in enumerate(frontier):
                    if item.value.compare_boards(child.value) and item.path_cost > child.path_cost:
                        frontier[i] = child

    


    
