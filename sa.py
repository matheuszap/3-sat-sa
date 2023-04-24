with open("uf20-01.cnf", "r") as f:
    for i, line in enumerate(f):
        if i >= 8:  # Inicia leitura a partir da linha 9 (índice 8)
            variables = line.split()
            if len(variables) == 4:  # Verifica se existem 4 variáveis na linha
                var1, var2, var3, var4 = variables
                # Faça algo com as variáveis, por exemplo, imprimi-las
                print(var1, var2, var3, var4)