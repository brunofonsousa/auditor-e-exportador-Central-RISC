# verifica se as pastão estão vazias
import os

log = open('Relação - Matriculas sem Imagem.txt', 'w')
lista_vazios = list()
pasta = os.listdir('C:/Users/BrUnO/Downloads/Matriculas/')
matriculas_vazias = list()
for g in pasta:
    pasta_um = os.listdir('C:/Users/BrUnO/Downloads/Matriculas/' + str(g))
    cont = len(pasta_um)
    if cont == 1 and "Thumbs.db" in pasta_um:
        #print(f'{g} = Vázia, sem imagens!')
        status = 'Matrícula nº ' + str(g) + ' = Vázia, sem imagens!'
        matriculas_vazias.append(g)
    else:
        #print(f'Processada...{pasta_um}')
        status = 'Matricula nº ' + str(g) + ' = Processada...'
        #print(len(pasta_um))
    print(status)
    log = open('Relação - Matriculas sem Imagem.txt', 'a+')
    log.writelines(status)
    log.writelines("\n")
    log.close()

'''
log = open('Relação - Matriculas sem Número (Ausentes).txt', 'w')
### verifica se todas as matriculas foram importadas e se falta alguma
# cria uma lista númerica das matriculas existentes para comparação
matriculas_existentes = list()
primeira_exist = 1
ultima_exist = #160000
for i in range(primeira_exist, ultima_exist + 1):
    matriculas_existentes.append(i)

# cria uma lista númerica das matrículas exportadas para comparação
exportadas = os.listdir('C:/Users/BrUnO/Downloads/Matriculas/')
matriculas_exportadas = list()
for i in exportadas:
    matriculas_exportadas.append(int(i))
lista_final = list(set(matriculas_existentes) - set(matriculas_exportadas))
lista_final = sorted(lista_final)

for i in lista_final:
    print(f'Matrícula ausente: {i}')
    log = open('Relação - Matriculas sem Número (Ausentes).txt', 'a+')
    log.writelines(status)
    log.writelines("\n")
    log.close()


'''
