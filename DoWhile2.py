'''Este programa cria um menu para executar no CMD'''

while True:
    print('1 - Cadastrar Pet')
    print('2 - Alterar cadastro de Pet')
    print('3 - Buscar Pet')
    print('4 - Apagar cadastro de Pet')
    print('5 - Sair do programa')

    opcao = int(input("Digite a opção desejada entre 1 e 5..."))

    if opcao >= 1 and opcao <= 5:
        if opcao == 5:
            print(f'Obrigado por usar nosso programa! ')
            break
        else:
            print(f'Você escolheu a opção {opcao}')
    else: 
        print('Não existe, digite uma opção válida! ')