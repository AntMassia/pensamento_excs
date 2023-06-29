
def perg():
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]

    respostas = []
    for i in perguntas:
        resposta = input(i + " (S/N): ")
        while resposta not in ["S", "N"]:
            print("Inválida. Responda com 'S' para Sim ou 'N' para Não.")
            resposta = input(i + " (S/N): ")
        respostas.append(resposta)

    return respostas

def main(respostas):
    quantidade_sim = respostas.count("S")

    if quantidade_sim == 2:
        return "Indiciduo Suspeito"
    elif quantidade_sim >= 3 and quantidade_sim <= 4:
        return "É um Cúmplice"
    elif quantidade_sim == 5:
        return "É o Assassino"
    else:
        return "Ele é Inocente"

respostas = perg()

classificacao = main(respostas)

print("Classificação: " + classificacao)
