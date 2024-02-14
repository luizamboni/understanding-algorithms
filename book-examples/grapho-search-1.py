grapho = {
    "jato": ["tato", "gato"],
    "tato": ["gato", "chato"],
    "gato": ["grato", "gado"],
    "chato": ["gado"],
    "gado": [],
}

init = "jato"
fim = "gado"

fila = [init]
ja_visitado = []

def e_o_fim(node):
    return node == fim

level = 0
while fila:
    tem_fim = False
    for item in fila:
        print(level, item)
        ja_visitado.append(item)

        if e_o_fim(item):
            print("achou!", item, level)
            tem_fim = True
            break
    
    if tem_fim:
        break

    
    nova_file = []
    for item in fila:

        sub_items = grapho[item]
        for item2 in sub_items:
            if item2 not in ja_visitado:
                nova_file.append(item2)

    fila = nova_file
    level += 1
