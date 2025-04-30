def irAteFiap(meio):
    if meio == 'ônibus':
       print('Tempo de cehegada em 1h')
    elif meio == 'metrô':
        print('Tempo de chegada e, 45min'):
    else:
        print('Acho que foi de helicoptero!')

meio = input('Digite a sua opção de transporte: \n')

irAteFiap(meio)              