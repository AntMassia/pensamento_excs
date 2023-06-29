import math

def raizz(n):
    if n < 0:
        print("Inválido!!!")
    else: 
        raiz = math.sqrt(n)
        print("A Raiz Quadrada de", n, "é Igual a:", raiz)

num = float(input("Digite um Número para Saber a sua Raiz: "))
raizz(num)
