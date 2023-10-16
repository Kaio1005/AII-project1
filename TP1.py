import algoritmos
import sys
import tabuleiro

algorithm = sys.argv[1]
count = 2
board_entries = []

solution = tabuleiro.Board([[1,2,3],[4,5,6],[7,8,0]], False)

for i in range (3):
    aux = []
    for j in range(3):
        aux.append(int(sys.argv[count]))
        count += 1
    board_entries.append(aux)

print_or_not = sys.argv[-1]

if print_or_not == "PRINT":
    board_1 = tabuleiro.Board(board_entries, True)
else:
    board_1 = tabuleiro.Board(board_entries, False)

if (algorithm == "B"):
    solution = algoritmos.BFS(board_1, solution)
elif (algorithm == "I"):
    solution = algoritmos.IDS(board_1, solution)
elif (algorithm == "U"):
    solution = algoritmos.UCS(board_1, solution)
elif (algorithm == "A"):
    solution = algoritmos.A_star(board_1, solution)
elif (algorithm == "G"):
    solution = algoritmos.GBFS(board_1, solution)

if solution is not None:
    print(solution.path_cost)
    print()
    if solution.value.print:
        nodes_to_print = []
        nodes_to_print.append(solution)
        parent = solution.parent_node
        while (parent != None):
            nodes_to_print.append(parent)
            parent = parent.parent_node
        
        nodes_to_print.reverse()

        for node in nodes_to_print:
            for i in range(len(node.value.board)):
                print(node.value.board[i])
            print()