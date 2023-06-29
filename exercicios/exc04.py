def contagem(numero):
    if numero == 0:
        print("Decolar!")
    else:
        print(numero)
        contagem(numero - 1)
        
num = int(input("Digite um número para iniciar a contagem regressiva: "))
contagem(num)
