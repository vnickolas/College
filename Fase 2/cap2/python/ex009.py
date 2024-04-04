

quantidade = int(input("Digite a quantidade de alimentos que você comeu: "))
total_kcal = float()

for x in range(0, quantidade):
    alimento = input("Digite o alimento que você comeu: ")
    calorias = float(input("Digite quantas Kcal (calorias):  "))
    print(f"O alimento {alimento} com {calorias} kcal foi adicionada(o)")
    total_kcal = total_kcal + calorias

print(f"Você consumiu um total de {total_kcal} calorias hoje!")