peso_total = float()
for x in range(1,5):
    peso_atual = float(input("Informe o peso da caixa atual em kg: "))
    print(f"Caixa de {peso_atual} kg adicionada")
    peso_total = peso_total + peso_atual
media = peso_total/5
print(f"O peso total de caixas é {peso_total}kg. A média de peso é {media}")
