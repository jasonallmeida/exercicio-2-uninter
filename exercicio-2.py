print('-'* 5 + ' Bem vindo a loja de marmitas do Jason L. Frazão de Almeida!'+  5 * '-') 
print('-'* 30 + ' Cardápio '+  30 * '-') # Realce 
print('-' * 35 + 35 * '-') 
 
#Criação do cardápio 
print('-----| Tamanho |   Bife Acebolado(BA)  |   Filé de Frango(FF)  |------') 
print('-----|    P    |         R$16.00       |         R$15.00       |------') 
print('-----|    M    |         R$18.00       |         R$17.00       |------') 
print('-----|    G    |         R$22.00       |         R$21.00       |------') 
print('-' * 35 + 35 * '-') 
 
acumulador = 0 #Variável para somar os valores dos pedidos 
 
while True: #Início do while 
 
    sabor = input('Entre com o sabor desejado (BA/FF): ') 
 
    if sabor == 'BA': # Início da condicional Bife Acebolado (BA) 
        tamanho = input('Entre com o tamanho desejado (P/M/G): ') 
 
        if tamanho == 'P': #Se tamanho for igual a P: 
            acumulador += 16.00 
            print('Você pediu um Bife Acebolado no tamanho P: R$16.00') 
            print('') #Espaço 
            opcao = input('Deseja mais alguma coisa? (S/N): ') 
            if opcao == 'S': 
                continue #Retornar para o ínício do laço 
            else: 
                break #Encerrar o laço 
 
        elif tamanho == 'M': #Se tamanho for igual a M: 
            acumulador += 18.00 
            print('Você pediu um Bife Acebolado no tamanho M: R$18.00') 
            print('')  # Espaço 
            opcao = input('Deseja mais alguma coisa? (S/N): ') 
            if opcao == 'S': 
                continue #Retornar para o ínício do laço 
            else: 
                break #Encerrar o laço 
 
        elif tamanho == 'G': #Se tamanho for igual a G 
            acumulador += 22.00 
            print('Você pediu um Bife Acebolado no tamanho G: R$22.00') 
            print('')  # Espaço 
            opcao = input('Deseja mais alguma coisa? (S/N): ') 
            if opcao == 'S': 
                continue #Retornar para o ínício do laço 
            else: 
                break #Encerrar o laço 
 
        else: #Senão: 
            print('Tamanho inválido! Tente novamente') # Fim da condicional Bife Acebolado (BA) 
            print('') #Espaço 
 
    # Início da condicional de Filé de Frango (FF) 
    elif sabor == 'FF': 
        tamanho = input('Entre com o tamanho desejado (P/M/G): ') 
 
        if tamanho == 'P': #Se tamanho for igual a P: 
            acumulador += 15.00 
            print('Você pediu um Filé de Frango no tamanho P: R$15.00') 
            print('')  # Espaço 
            opcao = input('Deseja mais alguma coisa? (S/N): ') 
            if opcao == 'S': 
                continue #Retornar para o ínício do laço 
            else: 
                break #Encerrar o laço 
 
        elif tamanho == 'M': #Se tamanho for igual a M: 
            acumulador += 17.00 
            print('Você pediu um Filé de Frango no tamanho M: R$17.00') 
            print('')  # Espaço 
            opcao = input('Deseja mais alguma coisa? (S/N): ') 
            if opcao == 'S': 
                continue #Retornar para o ínício do laço 
            else: 
                break #Encerrar o laço 
 
        elif tamanho == 'G': #Se tamanho for igual a G 
            acumulador += 21.00 
            print('Você pediu um Filé de Frango no tamanho G: R$21.00') 
            print('')  # Espaço 
            opcao = input('Deseja mais alguma coisa? (S/N): ') 
            if opcao == 'S': 
                continue #Retornar para o ínício do laço 
            else: 
                break #Encerrar o laço 
 
        else: #Senão: 
            print('Tamanho inválido! Tente novamente') # Fim da condicional Filé de Frango (FF) 
            print('') #Espaço 
    else: 
        print('Sabor inválido! Tente novamente.') 
        print('') #Espaço 
 
#Exibir o total a ser pago 
print(f'O valor total a ser pago: R$ {acumulador}') 