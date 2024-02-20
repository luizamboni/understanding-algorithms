def knapsack(values, weights, capacity):
    num_items = len(values)
    # Inicializa a matriz de soluções com zeros
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]
    
    for item_index in range(1, num_items + 1):
        for weight_limit in range(1, capacity + 1):
            current_weight = weights[item_index - 1]
            current_value = values[item_index - 1]
            
            # Verifica se o peso do item atual pode ser adicionado à mochila
            if current_weight <= weight_limit:
                value_with_item = current_value + dp_table[item_index - 1][weight_limit - current_weight]
                value_without_item = dp_table[item_index - 1][weight_limit]
                dp_table[item_index][weight_limit] = max(value_with_item, value_without_item)
            else:
                dp_table[item_index][weight_limit] = dp_table[item_index - 1][weight_limit]
    
    # Retorna o valor máximo que pode ser alcançado dentro da capacidade dada
    return dp_table[num_items][capacity]

# Exemplo de uso
item_values = [60, 100, 120]
item_weights = [10, 20, 30]
max_capacity = 50
max_value = knapsack(item_values, item_weights, max_capacity)
print(max_value)
