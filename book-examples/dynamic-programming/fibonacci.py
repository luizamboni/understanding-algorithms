def fibonacci(n):
    # Passo 1: Inicialização do array com os dois primeiros números de Fibonacci
    # O array 'fib' armazenará os números de Fibonacci calculados, com fib[0] = 0 e fib[1] = 1
    fib = [0, 1]
    
    # Passo 2: Cálculo iterativo dos números de Fibonacci
    # Começamos de 2 até 'n', pois já conhecemos os valores de fib[0] e fib[1]
    for i in range(2, n + 1):
        # O próximo número de Fibonacci é a soma dos dois anteriores
        print(fib)
        fib.append(fib[i-1] + fib[i-2])
    
    # Passo 3: Retornar o n-ésimo número de Fibonacci
    return fib[n]

# Exemplo de uso: calcular o 9º número de Fibonacci
print(fibonacci(9))

