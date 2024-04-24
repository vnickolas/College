PLAYSTATION = int()
XBOX = int()
NITENDO = int()
print(" 1 - (PLAYSTATION)\n 2 - (XBOX)\n 3 - (NITENDO)")

for i in range(5):
    print("Digite o número do console que você deseja: ")
    voto = int(input())  # Converte o voto para maiúsculas para facilitar a comparação
    if voto == 1:
        print("Você escolheu o console: PLAYSTATION")
        PLAYSTATION += 1
    elif voto == 2: 
        print("Você escolheu o console: XBOX")
        XBOX += 1
    elif voto == 3:
        print("Você escolheu o console: NITENDO")       
        NITENDO += 1
    else:
        print("Opção inválida! Seu voto será nulo.")
# FIM DO FOR


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