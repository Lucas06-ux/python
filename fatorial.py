fatorial = int(input('Digite um número para ver o resultado de seu fatorial: '))
contador = 1
limite = fatorial

while contador < limite:
    fatorial *= contador
    contador += 1
else:
 print(f'O fatorial de {limite} é {fatorial}')