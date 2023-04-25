matrix = []
num_rows = 0

with open("uf20-01.cnf", "r") as f:
    for i, line in enumerate(f):
        if i == 7:
            num_rows = int(line.split()[3])
            matrix = [[] for _ in range(num_rows)]
        elif i >= 8:
            variables = line.split()
            if len(variables) == 4:
                matrix[i-8] = [int(v) for v in variables]

print(matrix)
