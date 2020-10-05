import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt #Used in the comparison below

"""
    * Objetivo:     Gerar treinamento da imagem escolhida com base nas imagens do diretorio.
    * Argumentos:   Diretorio da pasta com as imagens
    * Retorno:      Booleano mostrando se deu certo ou não.
"""
def train(dirPath):
    print('\033[34m',"="*30,'Algoritmo para treinar o classificador\033[m')
    print(dirPath)
    dir_01 = dirPath + '/1/'
    dir_02 = dirPath + '/2/'
    dir_03 = dirPath + '/3/'
    dir_04 = dirPath + '/4/'

    # diretorio_0X corresponde a uma lista com nomes das imagens de cada pasta numerada de 1 a 4.
    # Para pegar a imagem, use a lista de nomes
    diretorio_01 = os.listdir(dir_01)
    diretorio_02 = os.listdir(dir_02)
    diretorio_03 = os.listdir(dir_03)
    diretorio_04 = os.listdir(dir_04)

    for imgWay in diretorio_01:
        print("imgWay = ",dir_01+imgWay)
        generatinMatrix(dir_01+imgWay)
    




def calculate():
    print('Algoritmo para calcular e exibir as caracteristicas')

def classificate():
    print('Algoritmo para classificar imagem/região')

"""
    * Objetivo:     Gerar uma matriz a partir da imagem
    * Argumentos:   Diretorio de localização da imagem
    * Retorno:      Matriz gerada pela imagem
"""
def generatinMatrix(imgPath):
    im2 = Image.open(imgPath).convert('RGB')                  
    im2 = np.array(im2) 
    
    for m in im2:
        for n in m:
            print("[",n,"]")
