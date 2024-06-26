import pygame
from sys import exit
pygame.init()


class Abertura:
    def abre(self, fundo, caption):
        pygame.mixer.init()
        cores = {"branco": (255, 255, 255), "azul": (0, 0, 200), "preto": (0, 0, 0), "vermelho": (200, 0, 0)}
        monitor = pygame.display.set_mode((800, 600))
        fundo = pygame.image.load(fundo)
        fundo = fundo.convert()
        pygame.display.set_caption(caption)
        continua = True
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Comic Sans", 45, bold=True)
        font = font.render("INICIAR", True, (cores['azul']))
        bgs = pygame.mixer_music
        bgs.load("rock.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer.fadeout(5)
        f_x = 2
        f_y = 2
        proxima = "principal"

        while continua:
            monitor.fill((cores["vermelho"]))
            monitor.blit(fundo, (0, 0))
            f_x = f_x * -1
            f_y = f_y * -1
            monitor.blit(font, ((800//2)+f_x, (600//2)+f_y))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        mouse_pos = e.pos
                        x, y = mouse_pos[0], mouse_pos[1]
                        if 407 < x < 594 and 316 < y < 344:
                            continua = False
                        if 407 < x < 594 and 400 < y < 440:
                            proxima = "recordes"
                            continua = False
            pygame.display.flip()
            clock.tick(3)
        pygame.mixer_music.unload()
        self.funcao = proxima
