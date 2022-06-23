#EXTRAI DATAS DOS ARQUIVOS
import os
import datetime
import time
import datetime
from datetime import date
diretorios = list()
diretorios = os.listdir('I:/imagens digitalizadas/Livro 2/')
#diretorios.remove('Sl1MWYEG.jpg')
data_diferencaum = 0
data_diferencadois = 0
for i in range(len(diretorios)):
    pasta = os.listdir('I:/imagens digitalizadas/Livro 2/' + str(diretorios[i]))
    data_maior = 0
    data_tupla = 0
    for c in range(len(pasta)):
        conversor_data = datetime.datetime.fromtimestamp(os.path.getmtime('I:/imagens digitalizadas/Livro 2/' + str(diretorios[i]) + '/' + str(pasta[c])))
        data = int(str(conversor_data.year) + str(conversor_data.month) + str(conversor_data.day))
        if data > data_maior:
            data_maior = data
            data_tupla = conversor_data.year, conversor_data.month, conversor_data.day
        data_hoje = date.today()
        data_hoje = data_hoje.year, data_hoje.month, data_hoje.day
        print(pasta[c], data)
    data_fim = data_hoje[2] - data_tupla[2]
    print('-------> ', diretorios[i], data_tupla, 'Diferença: ', data_fim)
    print('\n' * 5)
    time.sleep(5)


'''
data_hoje[0] - data_tupla[0]

'''



