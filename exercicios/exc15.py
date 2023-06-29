def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = power(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é igual a {resultado}")
