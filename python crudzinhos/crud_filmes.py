def adicionar(titulo, diretor, ano, duracao, avaliacao):
    if len(titulo) == 0:
        raise ValueError("Informe o título do filme")
    
    if len(diretor) == 0:
        raise ValueError("Informe o diretor do filme")
    
    if ano > 2023 or ano < 1894:
        raise ValueError("Registre apenas filmes entre 1895 e 2023")

    if duracao <= 0:
        raise ValueError("Informe uma duração válida")

    if avaliacao > 10 or avaliacao < 0:
        raise ValueError ("Informe uma nota válida")

    with open("filmes.csv", "a") as arquivo:
        arquivo.write(f"{titulo},{diretor},{ano},{duracao},{avaliacao}\n")

def editar(indice):
    with open("filmes.csv", "r") as arquivo:
        filmes = arquivo.readlines()

    if indice < 1 or indice > len(filmes):
        print("Índice inválido.")
        return

    novo_titulo = input("Novo titulo: ")
    diretor = input("Novo diretor: ")
    ano = int(input("Novo ano de lançamento: "))
    duracao = int(input("Nova duração: "))
    avaliacao = float (input("Nova avaliação: "))

    filmes[indice - 1] = f"{novo_titulo},{diretor},{ano},{duracao},{avaliacao}\n"

    with open("filmes.csv", "w") as arquivo:
        arquivo.writelines(filmes)

def deletar(indice):
    with open("filmes.csv", "r") as arquivo:
        filmes = arquivo.readlines()

    if indice < 1 or indice > len(filmes):
        print("Índice inválido.")
        return

    filmes.pop(indice - 1)

    with open("filmes.csv", "w") as arquivo:
        arquivo.writelines(filmes)

def filme_cadastrado(titulo):
    with open("filmes.csv", "r") as arquivo:
        filmes = arquivo.readlines()

    for linha in filmes:
        if linha.split(",")[0] == titulo:
            return True

    return False

def listar_filmes():
    with open("filmes.csv", "r") as arquivo:
        filmes = arquivo.readlines()

    for i, linha in enumerate(filmes):
        titulo, diretor, ano, duracao, avaliacao = linha.strip().split(",")
        print(f"{i+1}. {titulo} - {diretor} - {ano} - {duracao} mins - Avaliação: {avaliacao}")

while True:
    print("1 - Registrar")
    print("2 - Editar")
    print("3 - Deletar")
    print("4 - Listar")
    opcao = input("Opção: ")

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida.")
        continue

    if opcao == "1":
        titulo = input("Título do filme: ")
        diretor = input("Dirigido por: ")
        ano = int(input("Ano de lançamento: "))
        duracao = int(input("Duração (mins): "))
        avaliacao = float (input("Avaliação: "))
        adicionar (titulo, diretor, ano, duracao, avaliacao)
    elif opcao == "2":
        listar_filmes()
        indice = int(input("Qual o número do filme que deseja editar? "))
        editar(indice)
    elif opcao == "3":
        listar_filmes()
        indice = int(input("Qual o número do filme que deseja deletar? "))
        deletar(indice)
    elif opcao == "4":
        listar_filmes()

    print("Deseja continuar? (S/N)")
    resposta = input("Resposta: ").upper()
    if resposta != "S":
        break
