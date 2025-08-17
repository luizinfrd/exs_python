while True:
    print("Bem-vindo ao programa de divisão segura!")
    print("1 - Dividir dois números")
    print("2 - Sair")
    escolha = input("Escolha uma opção (1 ou 2): ")
    if escolha == '2':  # Sair do loop
        print("Saindo do programa. Até logo!")
        break
    elif escolha != '1':
        print("Opção inválida. Por favor, escolha 1 ou 2.")
    else:
        try:
            n1 = int(input("Digite o primeiro numero: "))
            n2 = int(input("Digite o segundo numero: "))
            operacao = n1 / n2

        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira números inteiros.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        else:
            print(f"O resultado é: {operacao}")
        finally:
            print("Operação concluída.")