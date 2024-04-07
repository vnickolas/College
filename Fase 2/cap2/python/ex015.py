# #solicitar distância e tempo
# distancia = float(input("Digite a distância percorrida"))
# tempo = float(input("Digite o tempo da viagem"))
# #calcular a velocidade média
# velocidade_media = distancia/tempo
# #exibir o resultado
# print("A velocidade média é {} km/h".format(velocidade_media))

#Função que calcula a velocidade média
def calcularVelocidadeMedia ():
    #solicitar distância e tempo
    distancia = float(input("Digite a distância percorrida: "))
    tempo = float(input("Digite o tempo da viagem: "))
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))
    
calcularVelocidadeMedia()

print("####################################")

#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))

#aqui começa o programa principal
distancia = float(input("Informe a distância agr"))
tempo = float(input("Informe o tempo"))

#chamando a função com valores definidos pelo programador
calcularVelocidadeMedia(distancia,tempo)