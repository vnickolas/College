valor_compra = input("Informe o valor da compra: R$ ")
cupom_desconto = input("Informe o cupom de desconto ou digite N para 'NÃO TEM': ")
valor_final = float(valor_compra)

if cupom_desconto.upper() == "NIVER10":
    valor_final = float(valor_compra) * 0.85
    print("Cupom aceito! Você recebeu 15% de desconto!")
elif cupom_desconto == "N":
    print("Sua compra não teve desconto")
    print(f"O valor final da compra foi de R$ {valor_final}")
else: 
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
    print("Sua compra não terá desconto")
print(f"O valor final da compra foi de R$ {valor_final}")