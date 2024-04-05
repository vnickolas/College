qtd = int(input("Digite quantas transações você teve no dia: "))
valor_total = float()
for x in range(0, qtd):
    valor_transacao = float(input(f"Digite qual foi o valor da {x+1}º transação: R$ "))
    valor_total += valor_transacao
    print(f"A {x+1}º, no valor de R$ {valor_transacao} reais, foi adicionada.")
print(f"O valor total de suas transações no dia de hoje, foi de R$ {valor_total} reais")