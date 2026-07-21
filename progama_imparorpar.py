numero = (input('digite um numero: '))

if numero.isdigit():
   numero_valido = int(numero)
   par = numero_valido %2 == 0 
   parimpa_texto = 'impar'
   

   if par:
       parimpa_texto = 'par'   
   print(f' o numero {numero_valido} e {parimpa_texto}')
    
else:
    print('voce nao digitou um numero ')



