grapho = {
    "inicio": { 
        "a": 6,
        "b": 2,
    },
    "a": {
        "fim": 1,
    },
    "b": {
        "a": 3,
        "fim": 5,
    },
    "fim": {}
}

custos = {
    **grapho["inicio"], 
    "fim": float("inf")
}

pais = {}
pais["fim"] = None
for key in grapho["inicio"].keys():
    pais[key] = "inicio"

processados = []

def ache_o_custo_mais_baixo(custos):
    nodo_mais_baixo = None
    custo_mais_baixo = float("inf")
    for node in custos.keys():
        if node not in processados and custos[node] < custo_mais_baixo:
            nodo_mais_baixo = node
            custo_mais_baixo = custos[node]

    return nodo_mais_baixo

# print(grapho)
# print(custos)
nodo = ache_o_custo_mais_baixo(custos)

while nodo is not None:
    print(nodo, processados)
    vizinhos = grapho[nodo]
    for vizinho in vizinhos.keys():
        print("vizinho", vizinho, "custa atualmente", custos[vizinho])
        print("custo do nó atual para o vizinho", grapho[nodo][vizinho])
        if grapho[nodo][vizinho] + custos[nodo] < custos[vizinho]:
            custos[vizinho] = grapho[nodo][vizinho] + custos[nodo]

    processados.append(nodo)
    nodo = ache_o_custo_mais_baixo(custos)

print(custos)