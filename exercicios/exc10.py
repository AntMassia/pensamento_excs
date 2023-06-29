def soma(tupla):
    prod = 1
    for elemento in tupla:
        prod *= elemento
    return prod

tupla = (9, -3, 12, 6, 34, -17)
prod = soma(tupla)
print("O Resultado da tupla", tupla, "é Igual:", prod)
