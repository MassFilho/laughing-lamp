import os

# Variavel lista:

lista = []

while True:
    print('Selecione uma opção:')
    entrada_inicial = input('[i]nserir [a]pagar [l]istar [s]air: ') # Imput d usuário

    if entrada_inicial == 'i':
        while True:
            os.system('cls')
            print('Digite um item ou digite "s" para sair:')
            entrada_item = input('Item à ser inserido: ') # Nome do item a ser inserido

            lista.append(entrada_item)
            print('Item adicionado')
            os.system('cls')
            if entrada_item == 's':
                lista.pop()
                break

    elif entrada_inicial == 'a':
        try:
            if bool(lista) == True:
                while True:
                    print('Digite um número ou digite "s" para sair:')
                    entrada_apagar = input('Índice (número) à ser apagado: ')
                    entrada_capturada = int(entrada_apagar)
                    sair = 's'
                    os.system('cls')
                    if entrada_capturada in range(len(lista)):
                        del lista[entrada_capturada]
                        print('Índice apagado')
                        print('Nova lista:')
                        indices = range(len(lista))
                        for indice in indices:
                            print(indice, lista[indice])
                    elif entrada_capturada == sair:
                        break
                    else:
                        print(f'Índice "{entrada_apagar}" não existe, tente consultar a Lista')
                        indices = range(len(lista))
                        for indice in indices:
                            print(indice, lista[indice])
                        break
            else:
                os.system('cls')
                print('Nenhum ítem na lista.')
        except:
            print('Digite apenas números inteiros.')

    elif entrada_inicial == 'l':
        if bool(lista) == True:
            indices = range(len(lista))
            os.system('cls')
            print('Lista de compras:')
            for indice in indices:
                print(indice, lista[indice])
        else:
            print('----------------------')
            print('Lista Vazia.')
            print('----------------------')

    elif entrada_inicial == 's':
        break
    
    else:
        print('Digite um comando válido ("i", "a" ou "l").')
