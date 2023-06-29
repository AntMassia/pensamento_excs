
def inverte(lista):
    if len(lista) <= 1:
        return lista
    else:
        return [lista[-1]] + inverte(lista[:-1])
        
listt = [1, 2, 3, 4, 5]
reverse = inverte(listt)
print(reverse) 

