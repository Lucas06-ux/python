idade = 0

print("Olá seja muito bem vindo(a). \n")
print("Aqui só poderá acessado se você tiver 18 anos ou mais. Porfavor, confirme suas credenciais. \n")
nome = str(input('Escreva o seu nome compelto: \n'))
idade = int(input('Digite a sua idade: \n'))

if idade >=18 :
 print(f"Olá {nome} que bom que acessou nosso programa. Você está apto para usar nosso programa pois tem {idade} anos! Aproveite. \n ")
else:
 print(f"Olá {nome}, verifiquei que você tem {idade} anos. Sinto muito mas você não consegue avançar além desse ponto. Obrigado! \n")

 
 
 num = int(input("número: "))
 

if num > 0:
    print("Positivo")
if num < 0:
    print("Negativo")
if num == 0:
    print("Zero")