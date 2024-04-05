valor_divida = float(input("Digite o valor da sua dívida: R$ "))
taxa_juros = int(0)
parcelas = int(1)
print(f"Total: R$ {valor_divida} reais; Juros: R$ {taxa_juros} reais; Número de parcelas: {parcelas}; Valor da parcela: R$ {valor_divida} reais")


taxa_juros = 10
parcelas = 3
for i in range(4):
    juros = valor_divida * taxa_juros / 100
    valor_total = valor_divida + juros
    valor_parcela = valor_total / parcelas

    print(f"Total: R$ {valor_total} reais; Juros: R$ {juros} reais; Número de parcelas: {parcelas}; Valor da parcela: R$ {valor_parcela:.2f} reais")

    taxa_juros += 5
    parcelas += 3