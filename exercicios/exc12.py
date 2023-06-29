
def roger(string):
    palavras = string.split('-')
    ordenadas = sorted(palavras)
    strings = '-'.join(ordenadas)
    return strings

char = "xbox-playstation-nintendo-atari"
resultado = roger(char)
print(resultado)
