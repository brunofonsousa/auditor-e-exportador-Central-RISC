### verifica se todas as matriculas foram importadas e se falta alguma
# cria uma lista númerica das matriculas existentes para comparação
import os
log = open('Relação - Matriculas sem Número (Ausentes).txt', 'w')
'''
matriculas_existentes = list()
primeira_exist = 1
ultima_exist = 160000
for i in range(primeira_exist, ultima_exist + 1):
    matriculas_existentes.append(i)
'''
matriculas_existentes = [1, 300, 600, 1000, 2000, 3000]
# cria uma lista númerica das matrículas exportadas para comparação
exportadas = os.listdir('C:/Users/BrUnO/Downloads/Matriculas/')
matriculas_exportadas = list()
for i in exportadas:
    matriculas_exportadas.append(int(i))
lista_final = list(set(matriculas_existentes) - set(matriculas_exportadas))
lista_final = sorted(lista_final)

for i in lista_final:
    print(f'Matrícula ausente: {i}')
    status = 'Matrícula ausente: ' + str(i)
    log = open('Relação - Matriculas sem Número (Ausentes).txt', 'a+')
    log.writelines(status)
    log.writelines("\n")
    log.close()

