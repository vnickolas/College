valor_divida = float(input("Digite o valor da sua dívida: R$ "))
print(f"Total: R$ {valor_divida} reais; Juros: R$ 0,00 reais; Número de parcelas: 1; Valor da parcela: R$ {valor_divida} reais")

taxa_juros = int(10)
parcelas = int(3)
for i in range(4):
    juros = valor_divida * taxa_juros / 100
    valor_total = valor_divida + juros
    valor_parcela = valor_total / parcelas
    print(f"Total: R$ {valor_total} reais; Juros: R$ {juros} reais; Número de parcelas: {parcelas}; Valor da parcela: R$ {valor_parcela:.2f} reais")
    taxa_juros += 5
    parcelas += 3