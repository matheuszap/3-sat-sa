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

def map_initial_solution(num_var, initial_solution):
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


matrix, num_var, num_rows = read_cnf("uf20-01.cnf")

print(matrix)
print("Número de variáveis: " + str(num_var))
print("Número de cláusulas: " + str(num_rows))

initial_solution = initial_random_solution(num_var)

map = map_initial_solution(num_var, initial_solution)

print(map)

result = evaluate_solution(initial_solution, map, matrix)

print("Número de cláusulas não satisfeitas: " + str(result))
