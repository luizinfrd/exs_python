# Objetivo: Pedir a idade do usuário em anos e calcular quantos dias ele já viveu.

# Instruções:

# 1. Peça ao usuário para digitar a sua idade em anos. A entrada será um texto (string).
# 2. Converta essa idade (que é um texto) para um número inteiro.
# 3. Multiplique a idade em anos por 365 para obter o número aproximado de dias.
# 4. Imprima a mensagem final mostrando a idade em dias.


idade = input("Digite sua idade em anos: \n")
idade_convertida = int(idade)

dias = idade_convertida * 365

print(f"A sua idade em dias é: {dias}\n")

