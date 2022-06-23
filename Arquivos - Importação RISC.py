# cria as pastas
import os
import shutil

diretorio = ('C:/Users/BrUnO/Downloads/Destino/')
primeira = 1
ultima = 500 - 1
# listas as pastas e identifica para quais irão cada uma
lista = list()
lista = os.listdir('C:/Users/BrUnO/Downloads/Matriculas')
lista_inteiros = list()
for i in lista:
    inteiro = int(i)
    lista_inteiros.append(inteiro)
lista_ordenada = sorted(lista_inteiros)
num_pastas_criadas = int(lista_ordenada[-1] / 500)
for y in range(num_pastas_criadas + 1):
    matricula = ""
    destino = ""
    os.mkdir(diretorio + str(primeira) + " a " + str(ultima))
    pasta = str(primeira) + " a " + str(ultima)
    for i in range(primeira, ultima):        
        for g in lista_ordenada:
            if i == g:
                matricula = 'C:/Users/BrUnO/Downloads/Matriculas/' + str(i)
                destino = 'C:/Users/BrUnO/Downloads/Destino/' + str(pasta)
                shutil.move(matricula, destino)
                print(matricula, destino)
    primeira += 500
    ultima += 500
    if primeira >= 500:
        primeira = ultima - 499


# localiza, extrai e apaga a pasta
lista_vazios = list()
pasta = os.listdir('C:/Users/BrUnO/Downloads/Destino/')
for g in pasta:
    pasta_um = os.listdir('C:/Users/BrUnO/Downloads/Destino/' + str(g))
    cont = len(pasta_um)
    if cont > 0:
        for t in pasta_um:
            pasta_dois = os.listdir('C:/Users/BrUnO/Downloads/Destino/' + str(g) + '/' + str(t))
            cont_pasta_dois = len(pasta_dois)
            if cont_pasta_dois == 0:
                lista_vazios.append(pasta_um)
            for y in pasta_dois:
                if y != "Thumbs.db":
                    arquivo = 'C:/Users/BrUnO/Downloads/Destino/' + str(g) + '/' + str(t) + '/' + str(y)
                    destino = 'C:/Users/BrUnO/Downloads/Destino/' + str(g)
                    deletada = 'C:/Users/BrUnO/Downloads/Destino/' + str(g) + '/' + str(t)
                    print(arquivo)
                    shutil.copy(arquivo, destino)
                    log = open('log_importacao.txt', 'a+')
                    log.writelines(arquivo)
                    log.writelines("\n")
                    log.close()
            shutil.rmtree(deletada)

        
        





    
    
