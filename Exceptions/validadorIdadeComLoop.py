while True:
    print("Bem-vindo ao validador de idade!")
    print("1 - Validar idade")
    print("2 - Sair")
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '2':  # Sair do loop
        print("Saindo do programa. Até logo!")
        break
    elif escolha != '1':
        print("Opção inválida. Por favor, escolha 1 ou 2.")
    else:
        try:
            idade = int(input("Digite sua idade: "))
            if idade <= 0:
                print("Idade inválida. Por favor, insira uma idade maior que zero.")
            else:
                print(f"Sua idade é: {idade} anos")
                break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro positivo para a idade.")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
    