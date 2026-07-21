hora = int(input('digite a hora: '))
bom_dia = 0 <= hora <= 11 
boa_tarde = 12 <= hora <= 17
boa_noite = 18 <= hora <= 23
 
if bom_dia:
    print('bom dia!')
elif boa_tarde:
    print('boa tarde! ')
elif boa_noite:
    print('boa noite! ')