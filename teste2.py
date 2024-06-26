import os

import pygame
from sys import exit
from time import sleep
from lancamento import Lancamento
import random
pygame.init()


def carregar_imagem_aleatoria():
    lista_arquivos_imagem = os.listdir("sprites")
    total = len(lista_arquivos_imagem)
    escolhida = lista_arquivos_imagem[random.randint(0, total)]
    arquivo = f"sprites/{escolhida}"
    return arquivo


