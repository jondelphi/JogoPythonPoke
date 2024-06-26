import math

class Lancamento:
    def calcular_posicao(forca=10, angulo=10, tempo=0):
        gravidade = 9.81
        angulo_rad = math.radians(angulo)
        velocidade_inicial_x = forca * math.cos(angulo_rad)
        velocidade_inicial_y = forca * math.sin(angulo_rad)
        posicao_inicial_x = 0
        posicao_inicial_y = 0
        posicao_x = posicao_inicial_x + velocidade_inicial_x * tempo
        posicao_y = posicao_inicial_y + velocidade_inicial_y * tempo - 0.5 * gravidade * tempo**2    
        return posicao_x, posicao_y









