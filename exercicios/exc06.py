def strings(lista, n):
    resultado = []
    for palavra in lista:
        if len(palavra) > n:
            resultado.append(palavra)
    return resultado

lista = [ "xbox", "playstation", "nintendo", "atari"]
n = 5
stringsmaiores = strings(lista, n)
print(stringsmaiores)
