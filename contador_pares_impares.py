print('Digite 0 para sair')
contador_pares=0
contador_impares=0
soma_pares=0
soma_impares=0
while True:
    numero=int(input('Digite um número:'))
    if numero == 0:
        break
    if numero % 2 == 0:
        contador_pares = contador_pares + 1
        soma_pares = soma_pares + numero
    else:
        contador_impares = contador_impares + 1
        soma_impares = soma_impares + numero
if contador_pares == 0:
    media_pares = 0
else:
    media_pares = soma_pares / contador_pares
if contador_impares == 0:
    media_impares = 0
else:
    media_impares = soma_impares / contador_impares
print(f'A quantidade de números pares foi de {contador_pares}, a soma entre eles é de {soma_pares} e a média entre eles é de {media_pares}')
print(f'A quantidade de números ímpares foi de {contador_impares}, a soma entre eles é de {soma_impares} e a média entre eles é de {media_impares}')
