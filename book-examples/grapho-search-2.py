grapho = {
    "jato": ["tato", "gato"],
    "tato": ["gato", "chato"],
    "gato": ["grato", "gado"],
    "chato": ["gado"],
    "gado": [],
    "grato": []
}

init = "jato"
fim = "gado"

fila = [init]
ja_visitado = []

def e_o_fim(node):
    return node == fim

while fila:
    print(fila)
    item = fila.pop(0)
    if e_o_fim(item):
        print(item, "encontrado")
        break
    
    ja_visitado.append(item)

    for subitem in grapho[item]:
        if subitem not in ja_visitado:
            fila.append(subitem)