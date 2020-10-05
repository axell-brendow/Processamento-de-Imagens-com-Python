import os

def train(dirPath):
    print('Algoritmo para treinar o classificador')
    print(dirPath)
    dir_01 = dirPath + '/1/'
    dir_02 = dirPath + '/2/'
    dir_03 = dirPath + '/3/'
    dir_04 = dirPath + '/4/'

    # diretorio_0X corresponde a uma lista com nomes das imagens de cada pasta numerada de 1 a 4.
    # Para pegar a imagem, use a lista de nomes.
    diretorio_01 = os.listdir(dir_01)
    diretorio_02 = os.listdir(dir_02)
    diretorio_03 = os.listdir(dir_03)
    diretorio_04 = os.listdir(dir_04)




def calculate():
    print('Algoritmo para calcular e exibir as caracteristicas')

def classificate():
    print('Algoritmo para classificar imagem/região')

