
def roger(lista):
    if type(lista) != list:
        raise ValueError("O argumento deve ser uma lista")

    elementos = []
    for elemento in lista:
        if lista.count(elemento) == 1:
            elementos.append(elemento)

    return elementos

try:
    numeros = input("Digite uma lista de números separados por espaço: ").split()
    numeros = [int(num) for num in numeros]
    resultado = roger(numeros)
    print("Elementos únicos da lista:", resultado)
except ValueError as error:
    print(error)
