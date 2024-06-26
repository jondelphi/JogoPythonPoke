import pygame

class Tela:
    def __init__(self, fundo, caption):
        self.cores = {"branco": (255, 255, 255), "azul": (0, 0, 200), "preto": (0, 0, 0), "vermelho": (200, 0, 0)}
        self.monitor = pygame.display.set_mode((800, 600))
        self.fundo = pygame.image.load(fundo)
        self.fundo = self.fundo.convert()
        pygame.display.set_caption(caption)

