
print("1 - CDB (Certificado de Depósito Bancário)\n2 - LCI (Letra de Crédito Imobiliário)\n3 - LCA (Letra de Crédito do Agronegócio)")

tipo_investimento = int(input("Digite o número correspondente ao investimento resgastado: "))
while tipo_investimento <= 0 or tipo_investimento >= 4:
    print("Valor inválido. Por favor, digitar uma das 3 opções válidas acima.")
    tipo_investimento = int(input("Digite o número correspondente ao investimento resgastado: "))

valor_imposto = float()
valor_resgatado = float(input("Digite o valor a ser resgatado: R$ "))
while valor_resgatado < 10:
    print("Valor inválido. Por favor, digitar um valor válido acima de R$ 10 reais.")
    valor_resgatado = float(input("Digite o valor a ser resgatado: R$ "))

if tipo_investimento == 2:
    tipo_investimento = "LCI"
    print(f"Você está restagatando uma aplicação {tipo_investimento}. O valor selecionado para resgate foi de R$ {valor_resgatado}. Considerando que a {tipo_investimento} é isenta de imposto, o valor final de resgate é de R$ {valor_resgatado} reais.")
elif tipo_investimento == 3:
    tipo_investimento = "LCA"
    print(f"Você está restagatando uma aplicação {tipo_investimento}. O valor selecionado para resgate foi de R$ {valor_resgatado}. Considerando que a {tipo_investimento} é isenta de imposto, o valor final de resgate é de R$ {valor_resgatado} reais.")
else:
    tipo_investimento = "CDB"
    dias_permanencia = int(input("Quantos dias o valor ficou investido?: "))

    if dias_permanencia <= 180:
        valor_imposto =  valor_resgatado * 22.5 / 100
        valor_final_resgate = valor_resgatado - valor_imposto

        print(f"Você está restagatando uma aplicação {tipo_investimento}. O valor selecionado para resgate foi de R$ {valor_resgatado}. Considerando a permanência de {dias_permanencia} dias, o valor do imposto a ser pago é de R$ {valor_imposto} reais e o valor final de resgate é de R$ {valor_final_resgate} reais.")

    elif dias_permanencia >= 181 and dias_permanencia <= 360:
        valor_imposto =  valor_resgatado * 20 / 100
        valor_final_resgate = valor_resgatado - valor_imposto

        print(f"Você está restagatando uma aplicação {tipo_investimento}. O valor selecionado para resgate foi de R$ {valor_resgatado}. Considerando a permanência de {dias_permanencia} dias, o valor do imposto a ser pago é de R$ {valor_imposto} reais e o valor final de resgate é de R$ {valor_final_resgate} reais.")

    elif dias_permanencia >= 361 and dias_permanencia <= 720:
        valor_imposto =  valor_resgatado * 17.5 / 100
        valor_final_resgate = valor_resgatado - valor_imposto

        print(f"Você está restagatando uma aplicação {tipo_investimento}. O valor selecionado para resgate foi de R$ {valor_resgatado}. Considerando a permanência de {dias_permanencia} dias, o valor do imposto a ser pago é de R$ {valor_imposto} reais e o valor final de resgate é de R$ {valor_final_resgate} reais.")

    else:
        valor_imposto =  valor_resgatado * 15 / 100
        valor_final_resgate = valor_resgatado - valor_imposto

        print(f"Você está restagatando uma aplicação {tipo_investimento}. O valor selecionado para resgate foi de R$ {valor_resgatado}. Considerando a permanência de {dias_permanencia} dias, o valor do imposto a ser pago é de R$ {valor_imposto} reais e o valor final de resgate é de R$ {valor_final_resgate} reais.")