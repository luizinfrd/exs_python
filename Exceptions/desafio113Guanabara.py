def leiaInt(n):
    while True:
        try:
            n = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro.")
        except Exception as e:
            print(f"Erro inesperado: {e}")  
        else:
            return n        
def leiaFloat(n):
    while True:
        try:
            n = float(input("Digite um número real: "))
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número real.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        else:
            return n
        


n = leiaInt(0)
f = leiaFloat(0)

print(f"Você digitou o número inteiro: {n} e o número float: {f}")
        