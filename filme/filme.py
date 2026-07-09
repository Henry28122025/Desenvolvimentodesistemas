def menu():
         print("0. Adicionar Filme (OPCIONAL)"),
         print("1. Listar Filmes"),
         print("2. Informações de um filme pelo titulo")
         print("3. Filmes de um Diretor específico"),
         print("4. Filmes de um Gênero específico"),
         print("5. Media de duração dos filmes"),
         print("6. Sair")

while menu():
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        adicionar_filme()
    elif opcao == "1":
        listar_filmes()
    elif opcao == "2":
        titulo = input("Digite o título do filme: ")
        informacoes_filme(titulo)
    elif opcao == "3":
        diretor = input("Digite o nome do diretor: ")
        filmes_diretor(diretor)
    elif opcao == "4":
        genero = input("Digite o gênero: ")
        filmes_genero(genero)
    elif opcao == "5":
        media_duracao()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        