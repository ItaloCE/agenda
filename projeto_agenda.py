agenda = {}
while True:
    print('---AGENDA TELEFONICA---')
    print('1 - Adicionar contato')
    print('2 - Editar telefone')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - Listar todos')
    print('Sair')
    opcao = input('Selecionar uma opção: ')
    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        if nome not in agenda:
          agenda[nome] = input(f'Digite o telefone de {nome}: ')
          print('Contato adicionado com sucesso!')
          print(agenda)
        else:
            print('Contato com este nome ja existe!')

    elif opcao == '2':
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            agenda[nome] = input(f'Digite o novo telefone de {nome}: ')
            print('Telefone alterado com sucesso!')
            print(agenda)
        else:
            print('Contato com este nome não existe!')

    elif opcao == '3':
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            del agenda[nome]
            print('Contato removido com sucesso!')
            print(agenda)
        else:
            print('Contato com este nome nao existe!')

    elif opcao == '4':
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            print(f'Telefone:{agenda[nome]}')
        else:
            print('Contado com este nome não existe:')

    elif opcao == '5':
        print('--- Todos os contatos ---')
        for key in agenda:
            print(f'Nome: {nome} - Telefone: {agenda[nome]}')

    elif opcao == '6':
        print('Você saiu do programa')
        break

    else:
        print('Opção inválida!')


