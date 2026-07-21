# variavel = (int(100500.10))
# print (f'{variavel: >20}')
# print (f'{variavel: >10}')
# print (float(f'{variavel}'))
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido} 
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('digite seu nome: ')                           
idade = input('digite sua idade: ')

if nome and idade:
    print(f'seu nome e: {nome} ')
    print(f'seu nome invertido e : {nome [::-1]}')

    if ' '  in nome:
        print('seu nome contem espacos') 
    else:
        print('seu nome nao contem espacos')            
    


    print(f'seu nome tem um total de letras:', len(nome))
    print(f'a primeira letra do seu nome e:', nome[0])
    print(f'a ultima letra do seu nome e:', nome[7])
else:
    print ('Desculpe, voce deixou campos vazios')
