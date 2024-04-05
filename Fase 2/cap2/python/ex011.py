
numero = int(input("Digite um número qualquer que você acredite que tenha sucesso: "))
fibonacci = int(0)
algoritimo = int(1)
fibonacci_lista = []

for x in range(0, numero+1, 1):
    print(f"{algoritimo}") # se algoritmo valer 5
    fibonacci_lista.append(algoritimo)
    algoritimo += fibonacci # algoritmo vai somar seu 5 + o 0 da fibo, onde algoritmo vai passar a ser 5 + 0
    fibonacci = algoritimo - fibonacci # fibo vai passar a ser o 5 - 0. Assim, vai ser PRINTADO O NÚMERO 5. Quando começar a ler de novo o for, vai ser lido que o algoritimo é 5, só que vai receber 5+5 (algo+fibo), o algoritmo vai valer 10, e vai ser PRINTADO O NÚMERO 5 de novo. E como a fibo é o algo-fibo (5-5), a fibo vai valer 5. SENDO ASSIM, no novo loop, vai ser que o algoritimo é 10, só que vai receber 10+5 (algo+fibo), o algoritmo vai valer 15 e como a fibo é o algo-fibo (15-5) vai ser PRINTADO O NÚMERO 15 e assim vai indo

if numero in fibonacci_lista:
    print("AÇÃO BEM-SUCEDIDA!") # QUANDO A PESSOA DIGITAR O NÚMERO QUE SE ENCONTRAR NO FINAL DA LISTA DA FIBO
else:
     print("A AÇÃO FALHOU!")
