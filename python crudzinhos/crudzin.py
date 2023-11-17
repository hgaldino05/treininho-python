def registrar(usuario, nome, idade, id, game_favorito, horas_jogadas):
    # Valida a idade
    if idade > 99 or idade < 0:
        raise ValueError("Idade deve ser um valor de 0 a 99")

    # Valida o ID
    if len(id) > 6:
        raise ValueError("ID deve conter no máximo 6 dígitos")

    # Abre o arquivo em modo de escrita
    with open("dados.csv", "a") as arquivo:
        # Escreve os dados no arquivo
        arquivo.write(f"{usuario},{nome},{idade},{id},{game_favorito},{horas_jogadas}\n")

def editar(usuario, nome, idade, id, game_favorito, horas_jogadas):
    # Valida a idade
    if idade > 99 or idade < 0:
        raise ValueError("Idade deve ser um valor de 0 a 99")

    # Valida o ID
    if len(id) > 6:
        raise ValueError("ID deve conter no máximo 6 dígitos")

    # Abre o arquivo em modo de leitura
    with open("dados.csv", "r") as arquivo:
        # Cria uma lista com os dados do arquivo
        dados = arquivo.readlines()

    # Define uma flag para controle de atualização
    atualizado = False

    # Cria uma lista temporária para armazenar as mudanças
    dados_atualizados = []

    # Encontra o registro do usuário
    for linha in dados:
        if linha.split(",")[0] == usuario:
            # Atualiza os dados do registro
            linha = f"{usuario},{nome},{idade},{id},{game_favorito},{horas_jogadas}\n"
            atualizado = True
        # Adiciona a linha à lista temporária
        dados_atualizados.append(linha)

    # Se o usuário não foi encontrado, emite uma mensagem
    if not atualizado:
        print("Usuário não encontrado.")
        return

    # Abre o arquivo em modo de escrita
    with open("dados.csv", "w") as arquivo:
        # Escreve os dados atualizados no arquivo
        arquivo.writelines(dados_atualizados)


def deletar(usuario):
    # Abre o arquivo em modo de leitura
    with open("dados.csv", "r") as arquivo:
        # Cria uma lista com os dados do arquivo
        dados = arquivo.readlines()

    # Encontra o registro do usuário
    for i, linha in enumerate(dados):
        if linha.split(",")[0] == usuario:
            # Remove o registro da lista
            dados.pop(i)

    # Abre o arquivo em modo de escrita
    with open("dados.csv", "w") as arquivo:
        # Escreve os dados atualizados no arquivo
        arquivo.writelines(dados)

def usuario_cadastrado(usuario):
    with open("dados.csv", "r") as arquivo:
        dados = arquivo.readlines()

    for linha in dados:
        if linha.split(",")[0] == usuario:
            return True

    return False

while True:
    # Escolha a operação desejada
    print("1 - Registrar")
    print("2 - Editar")
    print("3 - Deletar")
    opcao = input("Opção: ")

    # Valida a opção
    if opcao not in ["1", "2", "3"]:
        print("Opção inválida.")
        continue

    # Realiza a operação desejada
    if opcao == "1":
        usuario = input("Usuário: ")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        id = input("ID: ")
        game_favorito = input("Game favorito: ")
        horas_jogadas = int(input("Horas jogadas: "))
        registrar(usuario, nome, idade, id, game_favorito, horas_jogadas)
    elif opcao == "2":
        usuario = input("Usuário: ")
        if not usuario_cadastrado(usuario):
            print("Usuário não cadastrado.")
            continue
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        id = input("Novo ID: ")
        game_favorito = input("Novo game favorito: ")
        horas_jogadas = int(input("Novas horas jogadas: "))
        editar(usuario, nome, idade, id, game_favorito, horas_jogadas)
    elif opcao == "3":
        usuario = input("Usuário: ")
        if not usuario_cadastrado(usuario):
            print("Usuário não cadastrado.")
            continue
        deletar(usuario)

    # Pergunta se o usuário deseja continuar
    print("Deseja continuar? (S/N)")
    resposta = input("Resposta: ").upper()
    if resposta != "S":
        break

