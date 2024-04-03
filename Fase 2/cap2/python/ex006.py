PLAYSTATION = int()
XBOX = int()
NITENDO = int()
print(" 1 - (PLAYSTATION)\n 2 - (XBOX)\n 3 - (NITENDO)")

for i in range(5):
    print("Digite o número do console que você deseja: ")
    voto = int(input())  # Converte o voto para maiúsculas para facilitar a comparação
    if voto == 1:
        print(f"Você escolheu o console: PLAYSTATION")
    elif voto == 2: 
        print(f"Você escolheu o console: XBOX")
    else:
        print(f"Você escolheu o console: NITENDO")


 # Verifica o voto e atualiza o contador apropriado
    if voto == 1:
        PLAYSTATION += 1
    elif voto == 2:
        XBOX += 1
    elif voto == 3:
        NITENDO += 1
    else:
        print("Voto inválido! Por favor, escolha entre PLAYSTATION, XBOX ou NINTENDO.")

# Determina o console vencedor com base nos votos
if PLAYSTATION > XBOX and PLAYSTATION > NITENDO:
    console_vencedor = "PLAYSTATION"
    total_votos = PLAYSTATION
elif XBOX > PLAYSTATION and XBOX > NITENDO:
    console_vencedor = "XBOX"
    total_votos = XBOX
elif NITENDO > PLAYSTATION and NITENDO > XBOX:
    console_vencedor = "NINTENDO"
    total_votos = NITENDO
else:
    console_vencedor = "EMPATE"
    total_votos = PLAYSTATION  # ou qualquer outro contador, já que todos são iguais

# Exibe o resultado
if console_vencedor == "EMPATE":
    print("Houve um empate entre os consoles!")
else:
    print(f"O console vencedor é {console_vencedor} com {total_votos} votos!")