import os
import shutil
import os.path
'''
#CRIA AS PASTAS
diretorio = ('C:/Users/INMYP/OneDrive/Área de Trabalho/Destino/') # Diretório de destino
primeira = 1
ultima = 500 - 1
lista = list()
lista = os.listdir('C:/Users/INMYP/OneDrive/Área de Trabalho/Imagens do dia  30-03-2020/Livro 2/') # Diretório das imagens que estão avulsas
lista_inteiros = list()
for i in lista:
    arqemint = i[0:8]
    inteiro = int(arqemint)
    if inteiro not in lista_inteiros:
        lista_inteiros.append(inteiro)
lista_ordenada = sorted(lista_inteiros)
num_pastas_criadas = int(lista_ordenada[-1] / 500)
pastas = list()
for y in range(num_pastas_criadas + 1):
    pasta = str(primeira) + " a " + str(ultima)
    for t in range(primeira, ultima):   
        for g in lista_ordenada:
            if t == g:
                if pasta not in pastas:
                    pastas.append(pasta)
                    print(f"Pasta {pasta} criada com sucesso...")
    primeira += 500
    ultima += 500
    if primeira >= 500:
        primeira = ultima - 499
for d in range(len(pastas)):
    os.mkdir(diretorio + pastas[d])
'''
        
#COLOCA OS ARQUIVOS DENTRO DAS PASTAS
lista_imagens = os.listdir('I:/30.03.2020 a 13.04.2020/Imagens do período de  30-03-2020 à  13-04-2020/Livro 3/Imagens digitalizadas') # Pasta onde estão as imagens
lista_pastas= os.listdir('I:/imagens digitalizadas/Livro 3') # Diretório das pastas onde as imagens serão arquivadas
for img in lista_imagens:
    numero_img = int(img[0:8])
    for past in lista_pastas:
        d = past.split(' a ')
        ini = int(d[0])
        fim = ini + 499
        if numero_img > ini and numero_img < fim:
            existe = ''
            imagem = 'I:/30.03.2020 a 13.04.2020/Imagens do período de  30-03-2020 à  13-04-2020/Livro 3/Imagens digitalizadas/' + img # Nome da imagem
            destino = 'I:/imagens digitalizadas/Livro 3/' + past # Nome da pasta de destino
            deletada = 'I:/imagens digitalizadas/Livro 3/' + past + '/' + img # Imagem se existir será deletada
            existe = os.path.exists(deletada)
            if existe == True:
                os.remove(deletada) # Remove a imagem existente
            shutil.move(imagem, destino) # Move para a pasta a nova imagem
            print(imagem, ' -> ', destino)
print("Processo terminado...")


    
    
