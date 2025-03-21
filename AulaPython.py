#Algoritmo: Conversao_Reais_Dolares
'''Este programa foi desenvolvido para converter o valor Real en Dólar'''

reais=0
cotacao_dolar=0
conversao=0

print("Programa para converter reais em dólar \n")
reais = float(input("Digite o valor que quer converter (em reais): \n"))
cotacao_dolar= float(input("Digite a cotação do dólar de hoje \n"))

conversao = reais/cotacao_dolar 

print("Com esta quantia é possível comprar: ")
print(conversao)
print("dólares")

print("Obrigado por usar nosso programa!")