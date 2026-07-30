# variavéis
operador_valido = ("+","-","*","/")

# entrada 



# validação


while True:
      numero1 = input("digite um numero ou 'sair': ")
      if numero1.lower() == 'sair':
       print('saindo..')
      
       break
    
      while not numero1.isdigit():
       numero1 = input("primeiro numero é inválido. digite novamente ")


      numero2 = input('digite outro numero: ')
  
      while not numero2.isdigit():
         numero2 = input('o segundo numero é inválido, digite novamente')

      operador = input('digite um operador ("+","-","*","/"): ')

      while operador not in operador_valido:
          operador = input('operador invalido, digite novamente')

        
    
      numero1 = int(numero1)
      numero2 = int(numero2)

      if operador == "+":
            print(numero1 + numero2)
      elif operador == "-":
            print(numero1 - numero2)
      elif operador == "*":
            print(numero1 * numero2)
      elif operador == "/":
        if numero2 == 0:
           print('não é possível dividir por zero')     
        else:
           print(numero1 / numero2)






