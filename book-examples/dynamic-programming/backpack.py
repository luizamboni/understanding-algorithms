


def pick_the_best(items, capacity):
    solutions = []

    for _ in range(len(items) + 1):
        row = []
        for _ in range(capacity + 1):
            row.append(0)
        solutions.append(row)

    for i in range(1, len(items) + 1):
        item = items[i-1]
        print("item:", item)
        item_cost = item["c"]
        item_value = item["v"]
        for capacity_limit in range(1, capacity + 1):
            value_without_item = solutions[i-1][capacity_limit]
            # print(f"capacily slot is {capacity_limit}  and item's cost is {item_cost}")

            if item_cost <= capacity_limit:

                rest_cost = capacity_limit - item_cost
                # vai na linha anterior para pegar a melhor opção conhecida
                best_value_with_rest_cost = solutions[i-1][rest_cost]
                value_with_item = (
                    # valor do item
                    item_value + 
                    # valor da melhor combinação com o custo que sobrou
                    best_value_with_rest_cost
                )

                # a idéia aqui é se vale a pena colocar esse item ou é melhor
                # deixar como estava pois o custo de adicionar um item
                # pode ser ter que deixar uma combinação mais valiosa de fora
                solutions[i][capacity_limit] = max(
                    value_with_item, 
                    value_without_item
                )
            else:
                solutions[i][capacity_limit] = value_without_item


    for row in solutions:
        print(row)
        
    print("solution:", solutions[len(items)][capacity])
    return solutions[len(items)][capacity]


pick_the_best([
    { "c": 3, "v": 10, "n": "agua"  },
    { "c": 1, "v": 3, "n": "livros" },
    { "c": 2, "v": 9, "n": "comida" },
    { "c": 2, "v": 5, "n": "casaco" },
    { "c": 1, "v": 6, "n": "camera" },
], 6)


pick_the_best([
    { "c": 4, "v": 30, "n": "radio"  },
    { "c": 3, "v": 20, "n": "notebook" },
    { "c": 1, "v": 15, "n": "violao" },
    { "c": 1, "v": 20, "n": "iphone" },
    { "c": 1, "v": 10, "n": "mp3 player" },
], 4)