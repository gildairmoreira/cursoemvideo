soma = cont = 0
while True:
    num = int(input('Digite um numero (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} Valores, é a soma deles é {soma}')