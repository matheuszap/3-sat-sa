import math
import random

matrix = []
num_rows = 0
num_var = 0

def read_cnf(file_name):
    with open(file_name, "r") as f:
        for i, line in enumerate(f):
            if i == 7:
                num_var = int(line.split()[2])
                num_rows = int(line.split()[3])
                matrix = [[] for _ in range(num_rows)]
            elif i >= 8:
                variables = line.split()
                if len(variables) == 4:
                    matrix[i-8] = [int(v) for v in variables]
    return matrix, num_var, num_rows

def initial_random_solution(num_var):
    initial_solution = []
    for i in range(num_var):
        initial_solution.append(random.choice([0, 1]))
    return initial_solution

def map_solution(num_var, initial_solution):
    map = {}
    for i in range(num_var):
        var_name = 'v{}'.format(i+1)
        map[var_name] = initial_solution[i]
    return map

def evaluate_solution(solution, var_dict, matrix):
    # Inicializa o número de cláusulas não satisfeitas
    num_clausulas_nao_satisfeitas = 0

    # Percorre todas as cláusulas da matriz
    for clausula in matrix:
        # Verifica se pelo menos uma das três variáveis da cláusula é satisfeita
        if (solution[var_dict[f"v{abs(clausula[0])}"]] == 1 and clausula[0] > 0) or (solution[var_dict[f"v{abs(clausula[0])}"]] == 0 and clausula[0] < 0):
            continue
        elif (solution[var_dict[f"v{abs(clausula[1])}"]] == 1 and clausula[1] > 0) or (solution[var_dict[f"v{abs(clausula[1])}"]] == 0 and clausula[1] < 0):
            continue
        elif (solution[var_dict[f"v{abs(clausula[2])}"]] == 1 and clausula[2] > 0) or (solution[var_dict[f"v{abs(clausula[2])}"]] == 0 and clausula[2] < 0):
            continue
        # Se nenhuma variável satisfaz a cláusula, incrementa o contador de cláusulas não satisfeitas
        num_clausulas_nao_satisfeitas += 1

    # Retorna o número de cláusulas não satisfeitas
    return num_clausulas_nao_satisfeitas

def generate_neighbor(solution, num_var):
    # Calcula o número de variáveis a serem invertidas
    num_var_invertidas = max(1, int(num_var / 4))

    # Seleciona aleatoriamente um subconjunto de variáveis a serem invertidas
    indices_var_invertidas = random.sample(range(num_var), num_var_invertidas)

    # Cria uma cópia da solução inicial para ser modificada
    neighbor = solution.copy()

    # Inverte os valores das variáveis selecionadas
    for indice in indices_var_invertidas:
        neighbor[indice] = 1 - neighbor[indice]

    return neighbor

def simulated_annealing(initial_solution, var_dict, matrix, max_iter, t):
    current_solution = initial_solution
    current_score = evaluate_solution(current_solution, var_dict, matrix)
    best_solution = current_solution.copy()
    best_score = current_score

    for it in range(max_iter):
        temperature = (1 - it/max_iter) ** t

        # Gerar vizinho aleatório
        neighbor = generate_neighbor(current_solution, num_var)

        # Avaliar o vizinho
        neighbor_score = evaluate_solution(neighbor, var_dict, matrix)

        # Aceitar o vizinho com uma determinada probabilidade
        delta_score = neighbor_score - current_score
        if delta_score > 0 or random.uniform(0, 1) < math.exp(delta_score / temperature):
            current_solution = neighbor
            current_score = neighbor_score

        # Atualizar a melhor solução encontrada
        if current_score > best_score:
            best_solution = current_solution.copy()
            best_score = current_score

    return best_solution, best_score


matrix, num_var, num_rows = read_cnf("uf20-01.cnf")

print(matrix)
print("Número de variáveis: " + str(num_var))
print("Número de cláusulas: " + str(num_rows))
print("-------------------------------------------")
print("Solução Inicial:")
initial_solution = initial_random_solution(num_var)

map = map_solution(num_var, initial_solution)
print(map)

result = evaluate_solution(initial_solution, map, matrix)
true_clauses = num_rows - result

print("Número de cláusulas satisfeitas: " + str(true_clauses))
print("-------------------------------------------")
print("Vizinho:")
neighbor = generate_neighbor(initial_solution, num_var)

map_neighbor = map_solution(num_var, neighbor)

print(map_neighbor)
