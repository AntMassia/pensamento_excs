def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
            
        else:
            print("O Ano é Bissexto")
            return True
    else:
        print("O Ano não é Bissexto")
        return False
        
ano = 2032
resultado = bissexto(ano)
print(resultado) 

