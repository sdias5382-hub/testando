

nome = input('digite seu nome: ')

if nome.isalpha():
    quantidade_de_letras = len(nome)

    if quantidade_de_letras  <= 4: 
        print('seu nome é pequeno')
    elif quantidade_de_letras == 5:
        print('seu nome é normal')
    elif quantidade_de_letras >= 6:
        print('seu nome é grande ')
else:
    print('digite letras!')
          