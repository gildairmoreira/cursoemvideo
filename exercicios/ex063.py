#SEQUENCIA FIBONACCI USANDO SUBSTITUIÇAO DE TERMOS PARA "ANDAR"
n = int(input('Quantos termos quer mostrar: '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')
print('~'*30)
