entrada1 = eval(input('Digite o primeiro numero:'))
entrada2 = eval(input('Digite o segundo numero: '))

if entrada1 > entrada2:
    print(f'O maior número é o {entrada1}')
elif entrada2 > entrada1:
    print(f'O maior número é o {entrada2}')

entrada4 = eval(input('Digite a nota da P1: '))
entrada5 = eval(input('Digite a nota da P2: '))

media = 0
media = (entrada4 + entrada5) /2

if media < 5:
    print('Você está reprovado!')

else:
    print('Você está aprovado! ')    

    #Início
entrada = eval(input('Digite a nota: '))

if entrada >= 0 and entrada <=10:
  print(f'Sua nota {entrada} é válida! ')
else:
  print(f'Sua nota {entrada} é inválida! ')  

#Fim