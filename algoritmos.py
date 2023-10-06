import tree
import tabuleiro

def generate_children (node):
    zero_idx = node.value.find_zero()
    if node.value.check_move_up(zero_idx[0], zero_idx[1]):
        new_board = node.value.move_up(zero_idx[0], zero_idx[1])
        node.add_child(new_board, node.path_cost+1)
    if node.value.check_move_down(zero_idx[0], zero_idx[1]):
        new_board = node.value.move_down(zero_idx[0], zero_idx[1])
        node.add_child(new_board, node.path_cost+1)
    if node.value.check_move_left(zero_idx[0], zero_idx[1]):
        new_board = node.value.move_left(zero_idx[0], zero_idx[1])
        node.add_child(new_board, node.path_cost+1)
    if node.value.check_move_right(zero_idx[0], zero_idx[1]):
        new_board = node.value.move_right(zero_idx[0], zero_idx[1])
        node.add_child(new_board, node.path_cost+1)

def search_state (state, colection):
    for possible_state in colection:
        if possible_state.value.compare_boards(state) == True:
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
            explored.append(exploring)
            generate_children(exploring)
            
            for child in exploring.children:
                if (not(search_state(child.value, frontier)) or not(search_state(child.value, explored))):
                    if solution.compare_boards(child.value):
                        return (child)
                    else:
                        frontier.append(child)
    
def UCS (board, solution):
    tree_1 = tree.Tree(board,0)
    frontier = [tree_1.root]
    explored = []

    while(len(frontier) > 0):
        exploring = frontier.pop(0)
        if solution.compare_boards(exploring.value):
            return (exploring)
        explored.append(exploring)
        generate_children(exploring)

        for child in exploring.children:
            if (not(search_state(child.value, frontier)) or not (search_state(child.value, explored))):
                frontier.append(child)
            elif search_state(child.value, frontier):
                for i, state in enumerate(frontier):
                    if state.value.compare_boards(child.value) == True:
                        frontier[i] = child
                
def IDS (board, solution):
    tree_1 = tree.Tree(board, 0)

    max_depth = 0

    while True:
        frontier = [tree_1.root]
        explored = []

        while (len(frontier) > 0):
            exploring = frontier.pop(0)

            if solution.compare_boards(exploring.value):
                return exploring
            
            explored.append(exploring)
            if exploring.path_cost < max_depth:
                generate_children(exploring)
                for child in exploring.children:
                    if (not (search_state(child.value, explored)) or not (search_state(child.value, frontier))):
                        frontier.append(child)
            
        max_depth += 1

'''
def IDS (board, solution):
    #Change to iterative
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
''' 

    


    
