valor_carro = float(input("Digite o valor do carro: R$ "))
valor_final = float(valor_carro * 0.8)
vezes = int(6) #Sabemos que o número de parcelas é a tabuada do 6
valor_parcelado = float()
parcelas = float()

print(f"O valor final do carro à vista com desconto de 20% é de: R$ {valor_final:.2f} reais")

for x in range(0, 10, 1):
    valor_parcelado = valor_carro * (vezes / 2) / 100 + valor_carro # coloquei o número de parcelas  divido por 2, pois vi que a cada número de parcelas, o adicional é sua metade
    parcelas = valor_parcelado / vezes
    print(f"O preço final parcelado em {vezes}X é de R$ {valor_parcelado:.2f} reais, com parcelas de R$ {parcelas:.2f} reais")
    vezes += 6