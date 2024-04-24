
# #criação de uma lista com os nomes dos Jedi
# jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
# #incluindo um valor digitado no final da lista
# jedi.append(input("Digite o nome de um jedi: "))



        
# #A variável assumirá cada um dos valores da lista

# # jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
# # for i in range(len(jedi)):
# #     print(jedi[i])
#         #OOOOOOOOOOOOOU:

# for nome in jedi:
#     #para cada volta do loop, exibir o valor assumido
#     print(nome)

# print("####################################")

# #criação de uma lista com os nomes dos Jedi
# jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
# #incluindo um valor em uma posição específica da lista
# jedi.insert(2, "Luminara")
# #A variável assumirá cada um dos valores da lista
# for nome in jedi:
#     #para cada volta do loop, exibir o valor assumido
#     print(nome)

# print("####################################")

# #criação de uma lista com os nomes dos Jedi
# jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
# #incluindo um valor pelo usuário em uma posição específica da lista
# jedi.insert(2, input("Digite o nome de um Jedi"))
# #A variável assumirá cada um dos valores da lista
# for nome in jedi:
#     #para cada volta do loop, exibir o valor assumido
#     print(nome)

# print("####################################")

# #criação de uma lista com os nomes dos Jedi
# jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
# #Removendo um valor em uma posição específica
# jedi.pop(2)
# #A variável assumirá cada um dos valores da lista
# for nome in jedi:
#     #para cada volta do loop, exibir o valor assumido
#     print(nome)

# print("####################################")

#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#Removendo um valor específico da lista
jedi.remove("Yoda")

jedi = sorted(jedi, key=str.lower)
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

