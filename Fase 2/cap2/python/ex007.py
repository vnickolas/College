

print("1 - Basic;\n2 - Silver;\n3 - Gold;\n4 - Platinum;")
print("Digite o número do plano que deseja:")
plano_de_assinatura = int(input())
faturamento_mensal = float(input("Digite o seu faturamento mensal: R$ ")) 
valor_cobrado = float()

if plano_de_assinatura == 1:
    valor_cobrado = faturamento_mensal * 0.30 #30%
    print("Você escolheu a assinatura Basic!")
    print("Todo mês, sob seu faturamento, será cobrado 30%")
    print(f"Portanto, a cada mês de faturamento de R$ {faturamento_mensal}, será cobrado o valor de R$ {valor_cobrado}")
elif plano_de_assinatura == 2:
    valor_cobrado = faturamento_mensal * 0.20 #20%
    print("Você escolheu a assinatura Basic!")
    print("Todo mês, sob seu faturamento, será cobrado 20%")
    print(f"Portanto, a cada mês de faturamento de R$ {faturamento_mensal}, será cobrado o valor de R$ {valor_cobrado}")
elif plano_de_assinatura == 3:
    valor_cobrado = faturamento_mensal * 0.10 #10%
    print("Você escolheu a assinatura Basic!")
    print("Todo mês, sob seu faturamento, será cobrado 10%")
    print(f"Portanto, a cada mês de faturamento de R$ {faturamento_mensal}, será cobrado o valor de R$ {valor_cobrado}")
elif plano_de_assinatura == 4:
    valor_cobrado = faturamento_mensal * 0.05 #5%
    print("Você escolheu a assinatura Basic!")
    print("Todo mês, sob seu faturamento, será cobrado 5%")
    print(f"Portanto, a cada mês de faturamento de R$ {faturamento_mensal}, será cobrado o valor de R$ {valor_cobrado}")
else:
    print("Você escolheu um número inválido. Por favor, escolha novamente um número correspondendo à um plano existente.")