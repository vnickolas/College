#criando um dicionário com dados
dicionário = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
#removendo todos os itens do dicionário
dicionário.clear()
#exibindo o dicionário completo após a remoção
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))