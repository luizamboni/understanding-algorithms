def maximizar_ganhos_com_indices(valores):
    n = len(valores)
    if n == 0:
        return [], 0
    if n == 1:
        return [0], valores[0]
    if n == 2:
        return [0 if valores[0] > valores[1] else 1], max(valores[0], valores[1])
    
    # Inicializa o máximo de ganhos até o quarto i e os predecessores
    max_ganhos = [0] * n
    escolhas = [-1] * n  # -1 indica que nenhum quarto foi escolhido ainda

    print("max_ganhos", max_ganhos)
    # print("escolhas",escolhas)
    max_ganhos[0] = valores[0]
    max_ganhos[1] = max(valores[0], valores[1])
    escolhas[1] = 0 if valores[0] > valores[1] else 1

    print("max_ganhos", max_ganhos)
    
    # Calcula o máximo de ganhos para i de 2 até n-1
    # como zero e um já foram iniciados, agora percorre-se a list verificando os outros valores
    for i in range(2, n):
        # compara o item atual + acumukado
        # com o valor acumulado 
        # se ganho do item anterior for maior que a combinação
        if max_ganhos[i-1] > (max_ganhos[i-2] + valores[i]):
            max_ganhos[i] = max_ganhos[i-1]
            escolhas[i] = escolhas[i-1]
        else:
            max_ganhos[i] = max_ganhos[i-2] + valores[i]
            escolhas[i] = i
        print("max_ganhos", max_ganhos)

    
    print("max_ganhos", max_ganhos)
    # Reconstrói os índices dos quartos escolhidos
    indices = []
    i = n - 1
    while i >= 0:
        if escolhas[i] == i:
            indices.append(i)
            i -= 2  # Pula o quarto anterior pois não podemos ter quartos adjacentes
        else:
            i -= 1
    
    indices.reverse()  # Inverte para obter a ordem correta dos índices
    return indices, max_ganhos[-1]

# Valores de cada quarto do exemplo fornecido
valores = [3, 7, 2, 1, 60, 3]
print("valores:", valores)
print("")
indices_selecionados, ganho_maximo = maximizar_ganhos_com_indices(valores)
indices_selecionados, ganho_maximo

print(indices_selecionados, ganho_maximo)
