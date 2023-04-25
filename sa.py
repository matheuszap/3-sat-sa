import random

matrix = []
num_rows = 0
num_var = 0


def gerar_solucao_inicial_aleatoria(num_var):
    solucao_inicial = []
    for i in range(num_var):
        solucao_inicial.append(random.choice([-1, 1]))
    return solucao_inicial


def avaliar_solucao(solucao, matriz_clausulas):
    # Inicializa o número de cláusulas não satisfeitas
    num_clausulas_nao_satisfeitas = 0

    # Percorre todas as cláusulas da matriz
    for clausula in matriz_clausulas:
        # Verifica se pelo menos uma das três variáveis da cláusula é satisfeita
        if (solucao[abs(clausula[0])-1] == 1 and clausula[0] > 0) or (solucao[abs(clausula[0])-1] == 0 and clausula[0] < 0):
            continue
        elif (solucao[abs(clausula[1])-1] == 1 and clausula[1] > 0) or (solucao[abs(clausula[1])-1] == 0 and clausula[1] < 0):
            continue
        elif (solucao[abs(clausula[2])-1] == 1 and clausula[2] > 0) or (solucao[abs(clausula[2])-1] == 0 and clausula[2] < 0):
            continue
        # Se nenhuma variável satisfaz a cláusula, incrementa o contador de cláusulas não satisfeitas
        num_clausulas_nao_satisfeitas += 1

    # Retorna o número de cláusulas não satisfeitas
    return num_clausulas_nao_satisfeitas


with open("uf20-01.cnf", "r") as f:
    for i, line in enumerate(f):
        if i == 7:
            num_var = int(line.split()[2])
            num_rows = int(line.split()[3])
            matrix = [[] for _ in range(num_rows)]
        elif i >= 8:
            variables = line.split()
            if len(variables) == 4:
                matrix[i-8] = [int(v) for v in variables]

print(matrix)
print("Número de variáveis: " + str(num_var))
print("Número de cláusulas: " + str(num_rows))

solucao_inicial = gerar_solucao_inicial_aleatoria(num_var)
resultado_avaliacao = avaliar_solucao(solucao_inicial, matrix)

print("Número de cláusulas não satisfeitas: " + str(resultado_avaliacao))
