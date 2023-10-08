import algoritmos
import sys
import tabuleiro

board_1 = tabuleiro.Board([[8,6,7],[2,5,4],[3,0,1]], True)

solution = tabuleiro.Board([[1,2,3],[4,5,6],[7,8,0]], False)

solution = algoritmos.BFS(board_1, solution)

if solution is not None:
    print(solution.path_cost)
    if solution.value.print:
        nodes_to_print = []
        nodes_to_print.append(solution)
        parent = solution.parent_node
        while (parent != None):
            nodes_to_print.append(parent)
            parent = parent.parent_node
        
        nodes_to_print.reverse()

        for num, node in enumerate(nodes_to_print):
            print(f"Node {num}")
            for i in range(len(node.value.board)):
                print(node.value.board[i])
            print()
