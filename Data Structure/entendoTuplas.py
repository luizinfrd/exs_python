# 1. Cria a lista principal
turma = []

# 2. Cria as tuplas dos alunos (com as listas de notas)
aluno1 = ("João Silva", "15/03/2005", [8.5, 9.0])
aluno2 = ("Maria Souza", "22/07/2004", [9.0]) # Corrigido para ser uma lista!

# 3. Adiciona as tuplas à lista
turma.append(aluno1)
turma.append(aluno2)

print("Turma inicial:")
print(turma)
print("-" * 20)

# 4. Acessa e imprime o nome do primeiro aluno
print("Nome do primeiro aluno:", turma[0][0])
print("-" * 20)

# 5. Acessa a lista de notas do primeiro aluno e adiciona uma nova nota
print("Adicionando nova nota para João...")
turma[0][2].append(7.5)
print("Nova lista de notas de João:", turma[0][2])
print("Tupla de João após a mudança:", turma[0])
print("-" * 20)

# 6. Tenta alterar o nome do segundo aluno (Isso vai gerar um erro!)
# O programa vai parar a execução aqui e mostrar o erro, como esperado.
try:
    print("Tentando alterar o nome de Maria...")
    turma[1][0] = "Maria Oliveira"
except TypeError as e:
    print(f"ERRO! Isso é esperado. Mensagem do erro: {e}")
finally:
    print("\nEstado final da lista (não foi alterada devido ao erro):")
    print(turma)
