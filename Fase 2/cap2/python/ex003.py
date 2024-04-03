idade = int(input("Digite sua idade: "))
print("OBS: Caso não souber seus batimentos por minuto, digite a letra 'N'")
bpm = input("Digite seu BPM (Batimentos por minuto): ")

if bpm.upper() == "N":
    bpm = int(input("Coloque o dedo do meio e o indicador na lateral do seu pescoço e digite quantos batimentos você escutou no tempo de 15 segundos: "))
    bpm *= 4
    print(f"Seu BPM é de {bpm}.")
    bpm = int(bpm) 
    if idade <= 2 and bpm <= 140 and bpm >= 101:
        print("Seu BPM está bom. Em caso de dúvidas, consulte um médico")
    elif idade >= 3 and idade <= 17 and bpm <= 100 and bpm >= 80:
        print("Seu BPM está bom. Em caso de dúvidas, consulte um médico")
    elif idade >= 18 and idade <= 49 and bpm <= 79 and bpm >= 70:
        print("Seu BPM está bom. Em caso de dúvidas, consulte um médico")
    elif idade >= 50 and bpm <= 69:
        print("Seu BPM está bom. Em caso de dúvidas, consulte um médico")
else: 
    bpm = int(bpm) 
if idade <= 2 and bpm <= 140 and bpm >= 101:
    print("Seu BPM está bom. Em caso de dúvidas, consulte um médico")
elif idade >= 3 and idade <= 17 and bpm <= 100 and bpm >= 80:
    print("Seu BPM está bom. Em caso de dúvidas, consulte um médico")
elif idade >= 18 and idade <= 49 and bpm <= 79 and bpm >= 70:
    print("Seu BPM está bom. Em caso de dúvidas, consulte um médico")
elif idade >= 50 and bpm <= 69:
    print("Seu BPM está bom. Em caso de dúvidas, consulte um médico")
else:
    print("Seu BPM está fora do normal. Por favor, sugerimos que consulte-se com um médico.")