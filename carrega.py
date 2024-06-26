import pygame
import random
import os
class Carrega(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.carregar_imagem_aleatoria()


    def carregar_imagem_aleatoria(self):
        lista_arquivos_imagem = os.listdir("sprites")
        total = len(lista_arquivos_imagem)
        escolhida = lista_arquivos_imagem[random.randint(0, total)]
        arquivo = f"sprites/{escolhida}"
        return arquivo

    def define_pos(self):
        return random.randint(350, 700), random.randint(200,500)