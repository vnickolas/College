#variavel para armazenar o peso total das caixas
peso_total = 0.0
#loop para repetir por 100 vezes a solicitação de peso
for x in range(1,5):
    #para cada volta do loop, solicitar o peso da caixa
    peso_atual = float(input("Informe o peso da caixa atual em kg: "))
    print(f"Caixa de {peso_atual} kg adicionada")
    #para cada peso solicitado, somar ao peso total
    peso_total = peso_total + peso_atual
#ao final do loop, calculamos a média
media = peso_total/5
#exibição dos resultados!
print(f"O peso total de caixas é {peso_total}kg. A média de peso é {media}")
