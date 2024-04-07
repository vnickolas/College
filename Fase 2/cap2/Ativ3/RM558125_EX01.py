segunda = int(0)
terca = int(0)
quarta = int(0)
quinta = int(0)
sexta = int(0)

n_colaboradores = int(input("Informe a quantidade de colaboradores que votarão: "))
while n_colaboradores <= 0:
    print("Caso não tiver colaboradores, o programa se encerra por aqui! :)")
    n_colaboradores = int(input("Caso contrário, informe a quantidade de colaboradores que votarão: "))

dia_da_semana = int()
dia_vencedor = ""
total_votos = int(0)
print("1 - Segunda-feira\n2 - Terça-feira\n3 - Quarta-feira\n4 - Quinta-feira\n5 - Sexta-feira")

for x in range(1, n_colaboradores+1):
    dia_da_semana = int(input(f"Qual dia da semana o colaborador {x} deseja?: "))

    if dia_da_semana == 1:
        print(f"Voto na Segunda-feira")
        segunda += 1
    elif dia_da_semana == 2:
        print(f"Voto na Terça-feira")
        terca += 1
    elif dia_da_semana == 3:
        print(f"Voto na Quarta-feira")
        quarta += 1
    elif dia_da_semana == 4:
        print(f"Voto na Quinta-feira")
        quinta += 1
    elif dia_da_semana == 5:
        print(f"Voto na Sexta-feira")
        sexta += 1
    else: 
        print("Voto nulo")
        
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    dia_vencedor = "segunda"
    total_votos = segunda
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    dia_vencedor = "terça"
    total_votos = terca
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    dia_vencedor = "quarta"
    total_votos = quarta
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    dia_vencedor = "quinta"
    total_votos = quinta
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    dia_vencedor = "sexta"
    total_votos = sexta
else:
    dia_vencedor = "EMPATE"


if dia_vencedor == "EMPATE":
    print("Houve um empate entre os dias da semana!")
else:
    print(f"O dia vencedor foi {dia_vencedor}-feira com {total_votos} votos!")