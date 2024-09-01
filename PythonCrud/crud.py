usuarios = {}
opcao = input("Qual ação deseja realizar? " +
              "<I> Incluir User\n" +
              "<P> Pesquisar User\n" +
              "<E> Excluir User\n" +
              "<L> Listar Users: \n").upper()

while opcao in ["I", "P", "E", "L"]:
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        nome = input("Digite o nome: ")
        data = input("Informe a última data de acesso: ")
        estacao = input("Por onde foi efetuado o último acesso? ")
        usuarios[chave] = [nome, data, estacao]

    elif opcao == "L":
        print(usuarios)

    elif opcao == "P":
        chave = input("Digite o login do user que quer pesquisar: ").upper()
        if chave in usuarios:
            print(f"Dados do usuário {chave}: {usuarios[chave]}")
        else:
            print("Usuário não encontrado.")

    elif opcao == "E":
        chave = input("Digite o login do usuário a ser excluído: ").upper()
        if chave in usuarios:
            del usuarios[chave]
            print(f"Usuário {chave} excluído com sucesso.")
        else:
            print("Usuário não encontrado.")

    opcao = input("O que deseja fazer?\n" +
                  "<I> Incluir User\n" +
                  "<P> Pesquisar User\n" +
                  "<E> Excluir User\n" +
                  "<L> Listar Users: \n").upper()