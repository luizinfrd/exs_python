# Objetivo: Pedir o preço de um produto e um percentual de desconto, e calcular o preço final após o desconto. O preço pode ter centavos.

# Instruções:

# 1. Peça ao usuário para digitar o preço original do produto (pode ser com vírgula, por exemplo, "49.99"). A entrada será um texto (string).
# 2. Converta esse preço (que é um texto) para um número com vírgula (float).
# 3. Peça ao usuário para digitar o percentual de desconto (por exemplo, "10" para 10%). A entrada será um texto (string).
# 4. Converta o percentual de desconto para um número inteiro.
# 5. Calcule o valor do desconto: (preço_original * percentual_desconto) / 100.
# 6. Calcule o preço final: preço_original - valor_desconto.
# 7. Imprima o preço original, o percentual de desconto e o preço final formatado com duas casas decimais.


preco = input("Digite o preço do seu produto: ")
preco_convertido = float(preco)

percentual_desconto = input("Digite o percentual de desconto: ")
desconto_convertido = int(percentual_desconto)

valor_desconto = (preco_convertido * desconto_convertido) / 100
preco_final = preco_convertido - valor_desconto

print(f"O preço original é: R$ {preco_convertido}\n")
print(f"O percentual de desconto é: {percentual_desconto}% \n")

#Formatação do preço final com duas casas decimais
print(f"O preço final é: R$ {preco_final:.2f}\n")

