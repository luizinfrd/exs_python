votos = ['candidato_A', 'candidato_B', 'candidato_A', 'candidato_C', 'candidato_B', 'candidato_A']

# 1. Usando um conjunto para encontrar candidatos únicos
candidatos_unicos = set(votos)
print("--- Candidatos Únicos ---")
print(candidatos_unicos)

# 2. Usando um dicionário para a contagem de votos
contagem_votos = {} # Dicionário vazio para começar

for voto in votos: # Renomeei a variável para 'voto' para ser mais claro
    if voto in contagem_votos:
        # Se o candidato já está no dicionário, incrementa a contagem
        contagem_votos[voto] += 1
    else:
        # Se o candidato não está, adiciona ele com a contagem inicial de 1
        contagem_votos[voto] = 1
        
print("\n--- Contagem de Votos ---")
print(contagem_votos)

