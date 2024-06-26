import pygame
from sys import exit
pygame.init()


class Fim:
    def abre(self, fundo, caption):
        pygame.mixer.init()
        cores = {"branco": (255, 255, 255), "azul": (0, 0, 200), "preto": (0, 0, 0), "vermelho": (200, 0, 0)}
        monitor = pygame.display.set_mode((800, 600))
        fundo = pygame.image.load(fundo)
        fundo = fundo.convert()
        move = 1
        pygame.display.set_caption(caption)
        continua = True
        over = pygame.image.load("gameover.jpg")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Comic Sans", 45, bold=True)
        font = font.render("Pressione Espaço pra continuar", True, (cores['branco']))
        bgs = pygame.mixer_music
        bgs.load("gameover.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer.fadeout(5)
        f_x = 2
        f_y = 2

        while continua:
            move *= -1
            monitor.fill((cores["branco"]))
            monitor.blit(fundo, (0, 0))
            monitor.blit(over, (70+move, 250+move))
            f_x = f_x * -1
            f_y = f_y * -1
            monitor.blit(font, (50+f_x, 500))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        continua = False
            pygame.display.flip()
            clock.tick(3)
        pygame.mixer_music.unload()
        self.funcao = "abertura"
