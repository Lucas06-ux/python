varSaida = False

while varSaida != True:
  print('Bem vindo a nossa calculadora Py! \n')
  print('Selecione entre as opções abaixo: \n')
  print('1 - Soma \n')
  print('2 - Subtração \n')
  print('3 - Multiplicação \n')
  print('4 - Divisão \n')
  print('5 - Sair \n')

  varOpcao = int(input('Digite a opção desejada: '))
  print('\n')

  match varOpcao:
    case 1:
      print('Você selecionou a opção Somar \n')
      varNum1 = float(input('Digite o primeiro número: '))
      varNum2 = float(input('Digite o segundo número: '))
      varSoma = varNum1 + varNum2
      print(f'O resultado da soma entre {varNum1} e {varNum2} é: {varSoma}')
      #os.system('cls')
      #os.system('clear')
    case 2:
      print('Você selecionou a opção Subtrair \n')
      varNum1 = float(input('Digite o primeiro número: '))
      varNum2 = float(input('Digite o segundo número: '))
      varSub = varNum1 - varNum2
      print(f'O resultado da subtração entre {varNum1} e {varNum2} é: {varSub}')
      #os.system('cls')
      #os.system('clear')
    case 3:
      print('Você selecionou a opção Multiplicar \n')
      varNum1 = float(input('Digite o primeiro número: '))
      varNum2 = float(input('Digite o segundo número: '))
      varMult = varNum1 * varNum2
      print(f'O resultado da multiplicação entre {varNum1} e {varNum2} é: {varMult}')
      #os.system('cls')
      #os.system('clear')
    case 4:
      print('Você selecionou a opção Dividir \n')
      varNum1 = float(input('Digite o primeiro número: '))
      varNum2 = float(input('Digite o segundo número: '))
      varDiv = varNum1 / varNum2
      print(f'O resultado da divisão entre {varNum1} e {varNum2} é: {varDiv}')
      #os.system('cls')
      #os.system('clear')
    case 5:
      print('Você selecionou a opção Sair \n')
      varSaida = True
