import pygame
from sys import exit
pygame.init()


class Recordes:
    def abre(self, caption):
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
        proxima = "abertura"

        while continua:
            monitor.fill((cores["vermelho"]))
            monitor.blit(fundo, (0, 0))
            monitor.blit(font, ((800//2 ), (600//2)))
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
        self.funcao = proxima
