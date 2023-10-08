import tree
import tabuleiro
import random

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

def search_state (state, colection, return_idx = False):
    for i, possible_state in enumerate(colection):
        if possible_state.value.compare_boards(state) == True:
            if (return_idx):
                return (i, True)
            else:
                return True
    if return_idx:
        return (None,False)
    else:
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
                if (not(search_state(child.value, frontier)) and not(search_state(child.value, explored))):
                    if solution.compare_boards(child.value):
                        return (child)
                    else:
                        frontier.append(child)

#need changes, priority queue not a simple queue, what is the cost in that case?
def UCS (board, solution):
    tree_1 = tree.Tree(board,0)
    frontier = [tree_1.root]
    explored = []

    while(len(frontier) > 0):
        exploring, exploring_idx = select_next (frontier)
        if solution.compare_boards(exploring.value):
            return (exploring)
        frontier.pop(exploring_idx)
        explored.append(exploring)
        generate_children(exploring)

        for child in exploring.children:
            if (not(search_state(child.value, frontier)) and not (search_state(child.value, explored))):
                frontier.append(child)
            elif search_state(child.value, frontier):
                for i, state in enumerate(frontier):
                    if state.value.compare_boards(child.value) == True and child.path_cost < state.path_cost:
                        frontier[i] = child


def IDS (board, solution, max_depth):
    #Change to iterative
    limit = 0
    tree_1 = tree.Tree(board, 0)

    while limit < max_depth:
        result = DFS(tree_1.root, solution, limit)

        if result != None:
            return result
    
    return None

def DFS (node, solution, limit):
    if solution.compare_boards(node.value):
        return (node)
    else:
        frontier = [node]
        explored = []
        while(len(frontier) > 0):
            exploring = frontier.pop(0)
            if exploring.path_cost < limit:
                explored.append(exploring)
                generate_children(exploring)
            
                for child in exploring.children:
                    if (not(search_state(child.value, frontier)) and not(search_state(child.value, explored))):
                        if solution.compare_boards(child.value):
                            return (child)
                        else:
                            frontier.append(child)

def manhattan_distance (node, piece_i, piece_j):
    piece = node.value.board[piece_i][piece_j]

    if piece == 0:
        manhattan_distance = abs(piece_i-(len(node.value.board)-1)) + abs(piece_j-(len(node.value.board[0])-1))
    else:
        count = 0

        for k in range (len(node.value.board)):
            for l in range (len(node.value.board[0])):
                count += 1
                if count == piece:
                    actual_place = (k,l)
                    break
        
        manhattan_distance = abs(piece_i-actual_place[0]) + abs(piece_j-actual_place[1])

    return manhattan_distance

def sum_distances (node):
    heuristic = 0

    for i in range(len(node.value.board)):
        for j in range(len(node.value.board[0])):
            heuristic += manhattan_distance (node, i, j)
    
    return heuristic

def select_next (frontier):
    selected = None
    selected_idx = None
    for i, node in enumerate(frontier):
        if selected == None:
            selected = node
            selected_idx = i
        elif node.f < selected.f:
            selected = node
            selected_idx = i
    
    return (selected, selected_idx)


#heuristic = manhattan distance sum
def A_star (board, solution):
    tree_1 = tree.Tree(board, 0)
    f = tree_1.root.path_cost + sum_distances(tree_1.root)
    tree_1.root.set_f (f)

    frontier = [tree_1.root]
    explored = []

    while (len(frontier) > 0):
        exploring, exploring_idx = select_next (frontier)

        if solution.compare_boards(exploring.value):
            return exploring
        
        frontier.pop(exploring_idx)

        explored.append(exploring)

        generate_children(exploring)

        for child in exploring.children:
            if not(search_state(child.value, explored)):
                child_idx, found = search_state(child.value, frontier, True)
                if not found:
                    f = child.path_cost + sum_distances(child)
                    child.set_f(f)
                    frontier.append(child)
                elif child.path_cost < frontier[child_idx].path_cost:
                    f = child.path_cost + sum_distances(child)
                    child.set_f(f)
                    frontier[child_idx] = child


def count_misplaced (node):
    count = 0
    misplaced = 0
    for i in range (len(node.value.board)):
        for j in range (len(node.value.board[0])):
            count += 1
            if node.value.board[i][j] != count:
                misplaced += 1
            
            if node.value.board[i][j] == 0 and (i!= (len(node.value.board)-1) or j != (len(node.value.board[0])-1)):
                misplaced += 1
    
    return misplaced


#heuristic = num pieces misplaced
def GBFS (board, solution):
    tree_1 = tree.Tree(board, 0)
    f = tree_1.root.path_cost + count_misplaced(tree_1.root)
    tree_1.root.set_f (f)

    frontier = [tree_1.root]
    explored = []

    while (len(frontier) > 0):
        exploring, exploring_idx = select_next (frontier)

        if solution.compare_boards(exploring.value):
            return exploring
        
        frontier.pop(exploring_idx)

        explored.append(exploring)

        generate_children(exploring)

        for child in exploring.children:
            if (not(search_state(child.value, explored)) and not (search_state(child.value, frontier))):
                f = child.path_cost + sum_distances(child)
                child.set_f(f)
                frontier.append(child)



def hill_climbing (board, k, max_it):
    tree_1 = tree.Tree(board, 0)
    f = count_misplaced(tree_1.root)
    tree_1.root.set_f(f)
    iteration = 0
    current_sol = tree_1.root

    while (iteration < max_it):
        generate_children(current_sol)

        best_child = None
        best_evaluation = current_sol.f

        for child in current_sol.children:
            f = count_misplaced(child)
            child.set_f (f)

            if child.f < best_evaluation:
                best_child = child
                best_evaluation = child.f
        
        if best_child is None:
            return current_sol
        
        if best_evaluation == current_sol.f:
            lateral_moves = 0
            while lateral_moves < k:
                random_neighbor = random.choice(current_sol.children)

                if random_neighbor.f < current_sol.f:
                    current_sol = random_neighbor
                    break

                lateral_moves += 1
        
        else:
            current_sol = best_child
        
        iteration += 1
    
    return current_sol
