# Objetivo: Você vai receber três números e precisa transformá-los em um texto para formar uma mensagem secreta.

# Instruções:

# 1. Peça ao usuário para digitar o primeiro número inteiro.
# 2. Peça ao usuário para digitar o segundo número inteiro.
# 3. Peça ao usuário para digitar o terceiro número inteiro.
# 4. Após receber os três números (que estarão como texto), converta cada um deles para um número inteiro.
# 5. Agora, transforme cada um desses números inteiros de volta em texto.
# 6. Concatene (junte) esses três textos, separados por um traço (-), para formar a "mensagem secreta".
# 7. Imprima a mensagem secreta.



def converterEDesconverter(x, y, z):
    converter1 = int(x)
    converter2 = int(y)
    converter3 = int(z)
    
    desconverter1 = str(converter1)
    desconverter2 = str(converter2)
    desconverter3 = str(converter3)
    
    print(f"Sua mensagem secreta é: {desconverter1}-{desconverter2}-{desconverter3}")
    
    
n1 = input("Digite o primeiro numero: \n")
n2 = input("Digite o segundo numero: \n")
n3 = input("Digite o terceiro numero: \n")

converterEDesconverter(n1, n2, n3)

    
    