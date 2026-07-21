velocidade_carros = int(input('qual a velocidade ? '))
local_carros = int(input('qual o local do carro ? '))


velocidade = velocidade_carros
local_carro = local_carros

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

carro_multado = velocidade >= RADAR_1 and local_carro >= (LOCAL_1 - RADAR_RANGE)

if carro_multado:
    print("multado")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
         local_carro <= (LOCAL_1 + RADAR_RANGE)and velocidade > RADAR_1:
    print ('carro multado em radar 1')
else:
    print('nao foi multado')



