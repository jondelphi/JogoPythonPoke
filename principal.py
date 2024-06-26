import pygame
from sys import exit
from lancamento import Lancamento
from carrega import Carrega
from time import sleep
import random
import os
pygame.init()


class Principal:
    def barra(self, tela):
        rect = pygame.Rect(70,480, 75, 20)
        pygame.draw.rect(tela,(255, 255, 255), rect)

    def barra2(self, tela):
        rect = pygame.Rect(70, 525, 90, 20)
        pygame.draw.rect(tela,(255, 255, 255), rect)

    
    def forca(self, tela, l, a):
        rect = pygame.Rect(70,525, l, a)
        pygame.draw.rect(tela,(255, 0, 0), rect)

    def angulo(self, tela, l, a):
        rect = pygame.Rect(70,480, l, a)
        pygame.draw.rect(tela, (255, 0, 0), rect)
        
    def run_principal(self,fundo, caption):
        pygame.mixer.init()
        cores = {"branco": (255, 255, 255), "azul": (0, 0, 200), "preto": (0, 0, 0), "vermelho": (200, 0, 0)}
        tecno = pygame.mixer_music
        tecno.load("sons/tecno.mp3")
        tecno.play(-1) 
       
        atingiu = False
        meu_x = 0
        cores = {"branco": (255, 255, 255), "azul": (0, 0, 200), "preto": (0, 0, 0), "vermelho": (200, 0, 0)}
        monitor = pygame.display.set_mode((800, 600))
        fundo = pygame.image.load(fundo)
        fundo = fundo.convert()
        pygame.display.set_caption(caption)
        continua = True
        sprite1 = pygame.image.load("ash/lanca1.png")
        sprite2 = pygame.image.load("ash/lanca2.png")
        sprite3 = pygame.image.load("ash/lanca2.png")
        sprite4 = pygame.image.load("ash/lanca4.png")
        pokebola = pygame.image.load("ash/poke-ball.png")
        pokebola = pokebola.convert()
        rect_bola = pokebola.get_rect()
        indice_sprite = 1
        x_sprite = 40
        y_sprite = 400
        bola_x = x_sprite+30
        bola_y = y_sprite+20
        rect_bola.x = bola_x
        rect_bola.y = bola_y
        clock = pygame.time.Clock()
        lanca = False
        tempo_atual = 0
        posicao = Lancamento
        meu_y = 0
        vidas = 5
        erro = 0
        primeira = 440
        forca = 10
        forca2 = 10
        aumenta = True
        aumenta2 = True
        press_angulo = False
        press_forca = False
        self.ang_definido = 10
        self.forca_definida = 10
        ash = pygame.image.load("ash/ash.png")
        vida = pygame.image.load("items/coracao.png")
        apagada = pygame.image.load("items/apagado.png")
        pokemons_pego = 0
        move = 1
        

        poke = Carrega()
        alvo = pygame.image.load(poke.image)
        alvo.convert()
        pos_alvo = poke.define_pos()
        rect_alvo = alvo.get_rect()
        rect_alvo.x = pos_alvo[0]
        rect_alvo.y = pos_alvo[1]
        vitoria = ['sons/parabens.mp3','sons/bom.mp3','sons/riso.mp3','sons/sim.mp3',
        'sons/sim2x.mp3','sons/simmestre.mp3','sons/sucesso.mp3']
        fundos = ["bg.jpg","floresta.jpg","03.jpg","04.jpg", "05.jpg",
         "06.jpg", "07.jpg","08.jpg","09.jpg", "nova2.jpg"]
        controlefundo=0

        while continua:
            move *= -1
            font = pygame.font.SysFont("Comic Sans", 28, bold=True)
            placar = str(pokemons_pego)
            font = font.render(placar, True, (cores['azul']))
            monitor.fill((cores["vermelho"]))
            monitor.blit(fundo, (0, 0))
            pygame.draw.rect(monitor,cores["branco"],(30, 102, 110, 25) )
            pygame.draw.circle(monitor,cores["branco"],(60, 80), 45)
            rect_alvo = alvo.get_rect()
            rect_alvo.x = pos_alvo[0]+move
            rect_alvo.y = pos_alvo[1]
            monitor.blit(alvo, rect_alvo)
            monitor.blit(font,(40,60))
            if vidas == 5:
                monitor.blit(vida,(440,40))
                monitor.blit(vida,(510,40))
                monitor.blit(vida,(580,40))
                monitor.blit(vida,(650,40))
                monitor.blit(vida,(720,40))
            if vidas == 4:
                monitor.blit(vida,(440,40))
                monitor.blit(vida,(510,40))
                monitor.blit(vida,(580,40))
                monitor.blit(vida,(650,40))
                monitor.blit(apagada,(720,40))
            if vidas == 3:
                monitor.blit(vida,(440,40))
                monitor.blit(vida,(510,40))
                monitor.blit(vida,(580,40))
                monitor.blit(apagada,(650,40))
                monitor.blit(apagada,(720,40))
            if vidas == 2:
                monitor.blit(vida,(440,40))
                monitor.blit(vida,(510,40))
                monitor.blit(apagada,(580,40))
                monitor.blit(apagada,(650,40))
                monitor.blit(apagada,(720,40))
            if vidas == 1:
                monitor.blit(vida,(440,40))
                monitor.blit(apagada,(510,40))
                monitor.blit(apagada,(580,40))
                monitor.blit(apagada,(650,40))
                monitor.blit(apagada,(720,40))
            if vidas == 0:
                monitor.blit(apagada,(440,40))
                monitor.blit(apagada,(510,40))
                monitor.blit(apagada,(580,40))
                monitor.blit(apagada,(650,40))
                monitor.blit(apagada,(720,40))
                continua = False
                
            
            monitor.blit(ash, (50, 60))  
            
            if atingiu:
                atingiu = False
                lanca = False
                indice_sprite = 1
                bola_x = 70
                bola_y = 420
                lanca = False
                tempo_atual = 0
                press_angulo = False
                press_forca = False
                atingiu = False
                continue
            self.barra(monitor)
            self.barra2(monitor)
            if not press_angulo:
                self.angulo(monitor, forca, 20)
            else:
                self.angulo(monitor, self.ang_definido, 20)

            if not press_forca:
                self.forca(monitor, forca2, 20)
            else:
                self.forca(monitor, self.forca_definida, 20)

            if aumenta:
                forca += 5
                if forca > 75:
                    aumenta = False
            else:
                forca -= 5
                if forca <= 10:
                    aumenta = True

            if aumenta2:
                forca2 += 5
                if forca2 > 90:
                    aumenta2 = False
            else:
                forca2 -= 5
                if forca2 <= 10:
                    aumenta2 = True
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_a:
                        print("Sair abertura")
                        continua = False
                    if e.key == pygame.K_l:
                        lanca = True
                        bola_x = 90
                        bola_y = 420
                    if e.key == pygame.K_SPACE:
                        if (press_angulo) and not(press_forca):
                            press_forca = True
                            self.forca_definida = forca2
                            lanca = True
                        if not press_angulo:
                            press_angulo = True
                            self.ang_definido = forca

            if lanca:
                if indice_sprite < 5:
                    indice_sprite += 1
            if indice_sprite > 5:
                lanca = False
                indice_sprite = 1
            if indice_sprite == 1:
                monitor.blit(sprite1, (x_sprite, y_sprite))
            elif indice_sprite == 2:
                monitor.blit(sprite2, (x_sprite, y_sprite))
            elif indice_sprite == 3:
                monitor.blit(sprite3, (x_sprite, y_sprite))
            elif indice_sprite == 4:
                monitor.blit(sprite4, (x_sprite, y_sprite))
            elif indice_sprite == 5:
                monitor.blit(sprite1, (x_sprite, y_sprite))
                lanca = False

                if bola_y < 800:
                    tempo_atual += 0.6
                    pos_xy = posicao.calcular_posicao(self.forca_definida,self.ang_definido, tempo_atual)
                    bola_x = 70 + pos_xy[0]
                    bola_y = 420 - pos_xy[1]
                    if rect_bola.colliderect(rect_alvo):
                        bola_x = 70
                        bola_y = 420
                        lanca = False
                        tempo_atual = 0
                        press_angulo = False
                        press_forca = False
                        poke = Carrega()
                        pokemons_pego += 1
                        alvo = pygame.image.load(poke.image)
                        alvo.convert()
                        pos_alvo = poke.define_pos()
                        rect_alvo = alvo.get_rect()
                        rect_alvo.x = pos_alvo[0]
                        rect_alvo.y = pos_alvo[1]
                        atingiu = True
                        bgs = pygame.mixer_music
                        vence = vitoria[random.randint(0,6)]
                        bgs.load(vence)
                        bgs.play(1)
                        sleep(4)
                        tecno = pygame.mixer_music
                        tecno.load("sons/tecno.mp3")
                        tecno.play(-1) 
                        controlefundo += 1
                        if controlefundo == 10:
                            controlefundo = 0
                        fundo = pygame.image.load(fundos[controlefundo])
                        fundo = fundo.convert()  
                        
                elif bola_y > 800:
                    indice_sprite = 1
                    bola_x = 70
                    bola_y = 420
                    lanca = False
                    tempo_atual = 0
                    press_angulo = False
                    press_forca = False
                    atingiu = False
                    vidas -= 1
                else:
                    bola_x = x_sprite + 50
                    bola_y = y_sprite + 10
                    atingiu = False

            rect_bola.center = (bola_x+10, bola_y+30)
            monitor.blit(pokebola, rect_bola)
            
            pygame.display.flip()
            clock.tick(10)
        self.funcao = "fim"
        pygame.display.flip()
