def menu():
    print("\n0. Adicionar Filme (OPCIONAL)")
    print("1. Listar Filmes")
    print("2. Informações de um filme pelo titulo")
    print("3. Filmes de um Diretor específico")
    print("4. Filmes de um Gênero específico")
    print("5. Media de duração dos filmes")
    print("6. Sair")

def contador_filme():
    palavra_chave = "Titulo:"
    
    try:   
        with open("filmes/estrutura-filmes.txt", encoding="utf-8") as r:
            conteudo = r.read()
        if palavra_chave in conteudo:
            texto_apos = conteudo.partition(palavra_chave)[2]
            print(f"Titulo:\n{texto_apos.strip()}")
        else:
            print("A palavra-chave não foi encontrada no arquivo.")
            
    except FileNotFoundError:
        print("Erro: O arquivo 'estrutura-filmes.txt' não foi encontrado.")



while True:
    menu()  
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        adicionar_filme()
    elif opcao == "1":
        contador_filme() 
    elif opcao == "2":
        informacoes_filmes()
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