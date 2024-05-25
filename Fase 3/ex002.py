#criando um dicionario com dados
dicionário = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o valor associado a uma chave específica
print(dicionário["R2-D2"])
#exibindo todos os valores em um dicionário
for valor in dicionário.values():
    print(valor)
    
print(dicionário.items())
    
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
    
