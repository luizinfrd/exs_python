def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def visualizar_tarefas(tarefas):
    if tarefas:
        for i, x in enumerate(tarefas, start=1):
            print(f"{i}- {x}")
    else:
        print("Nenhuma tarefa adicionada ainda.")

def buscar_tarefa(tarefas):
    try:
        indice_tarefa = int(input("Digite a tarefa que deseja buscar: "))
        
        for i, x in enumerate(tarefas,start=1):
            if indice_tarefa == i:
                print(f"Tarefa {i}: {x}")
                break
        else:
            print("Tarefa não encontrada. Por favor, verifique o número da tarefa.")
    except ValueError:
        print("Erro: Por favor, insira um número válido para a tarefa.")
    
    except IndexError:
        print("Erro: Tarefa não encontrada. Por favor, verifique o número da tarefa.")

    except Exception as e:
        print(f"Erro inesperado: {e}")

    finally:
        print("Busca de tarefa concluída.")

tarefas = []

while True:
    print("Bem-vindo ao Gerenciador de Lista de Tarefas!")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar lista de tarefas")
    print("3 - Escolha o número da tarefa para visualizar")
    print("4 - Sair")


    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_tarefa(tarefas)
    elif opcao == '2':
        visualizar_tarefas(tarefas)
    elif opcao == '3':
        buscar_tarefa(tarefas)   
    elif opcao == '4':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

