
def rogerio(lista):
    tamanho = len(lista)
    for i in range(tamanho - 1):
        trocas = False
        for n in range(tamanho - 1 - i):
            if lista[n][1] > lista[n + 1][1]:
                lista[n], lista[n + 1] = lista[n + 1], lista[n]
                trocas = True
        if not trocas:
            break
    return lista

lista = [(5, 7), (9, 2), (7, 2), (5, 4), (6, 3)]
ceni = rogerio(lista)
print(ceni)
