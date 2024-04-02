valor_bruto = float()
desconto = float()
valor_liquido = float()
valor_final = float()

print("Bem vindo a companhia área LATINA AMERICADA")
viajantes = int(input("Digite o número de pessoas (digite um se for só você): "))
print(" 1 - ECONOMICA;\n 2 - EXECUTIVA;\n 3 - PRIMEIRA CLASSE;\n") 
classe = float(input("Digite o número de qual classe você quer viajar: "))


if viajantes == 1 and classe == 1 :
    valor_bruto = 500
    desconto = 1
    valor_liquido = valor_bruto * desconto
    valor_final = valor_liquido * viajantes
    print(f"Sendo assim, será {viajantes} viajante na classe econômica.")
    print(f"O preço de cada passagem é de R$ {valor_bruto}. O desconto é garantido apenas para mais de um viajante por compra.")
    print(f"A compra dá um total de R$ {valor_final} reais.")
    print("Obrigado por comprar conosco! :D")
elif viajantes == 2 and classe == 1:
    valor_bruto = 500
    desconto = 0.97
    valor_liquido = valor_bruto * desconto
    valor_final = valor_liquido * viajantes
    print(f"Sendo assim, serão {viajantes} viajantes na classe econômica.")
    print(f"O preço de cada passagem é de R$ {valor_bruto}. Com o desconto de 3%, o valor cai para R${valor_liquido} para cada viajante.")
    print(f"A compra dá um total de R$ {valor_final} reais.")
    print("Obrigado por comprar conosco! :D")
    
elif viajantes == 3 and classe == 1:
    valor_bruto = 500
    desconto = 0.96
    valor_liquido = valor_bruto * desconto
    valor_final = valor_liquido * viajantes
    print(f"Sendo assim, serão {viajantes} viajantes na classe econômica.")
    print(f"O preço de cada passagem é de R$ {valor_bruto}. Com o desconto de 3%, o valor cai para R${valor_liquido} para cada viajante.")
    print(f"A compra dá um total de R$ {valor_final} reais.")
    print("Obrigado por comprar conosco! :D")
    
elif viajantes >= 4 and classe == 1:
    valor_bruto = 500
    desconto = 0.95
    valor_liquido = valor_bruto * desconto
    valor_final = valor_liquido * viajantes
    print(f"Sendo assim, serão {viajantes} viajantes na classe econômica.")
    print(f"O preço de cada passagem é de R$ {valor_bruto}. Com o desconto de 3%, o valor cai para R${valor_liquido} para cada viajante.")
    print(f"A compra dá um total de R$ {valor_final} reais.")
    print("Obrigado por comprar conosco! :D")
else:
    print("Você digitou uma classe errada.\n Volte e digite o número de qual classe você quer viajar")