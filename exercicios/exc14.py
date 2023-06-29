
def extrair_elemento(lista, n):
    elementos = []
    for tupla in lista:
        if len(tupla) > n:
            elementos.append(tupla[n])
        else:
            raise IndexError("Índice fora dos limites para pelo menos uma das tuplas")

    return elementos

try:
    lista_tuplas = [("Émily", 14), ("Jéssica", 19), ("Gabi", 24)]
    n = int(input("Digite o índice para extrair o elemento: "))
    resultado = extrair_elemento(lista_tuplas, n)
    print("Elementos extraídos:", resultado)
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
except IndexError as error:
    print(error)
